import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

class FFN(nn.Module):
    def __init__(self, in_dim, dim_hidden, out_dim, dropout, gelu_activation):
        super().__init__()
        self.dropout = dropout
        self.lin1 = nn.Linear(in_dim, dim_hidden)
        self.lin2 = nn.Linear(dim_hidden, out_dim)
        self.act = F.gelu if gelu_activation else F.relu


    def forward(self, input):
        x = self.lin1(input)
        x = self.act(x)
        x = self.lin2(x)
        x = F.dropout(x, p=self.dropout, training=self.training)
        return x
    
class FCN_LN(nn.Module):
    def __init__(self, hidden_dim, dropout, fcn_layers=2, gelu_activation=False):
        super().__init__()
        self.ffns = nn.ModuleList()
        self.layer_norm2 = nn.ModuleList()
        self.fcn_layers = fcn_layers

        for layer_id in range(self.fcn_layers):
            self.ffns.append(FFN(hidden_dim, hidden_dim, hidden_dim, dropout=dropout, gelu_activation=gelu_activation))
            self.layer_norm2.append(nn.LayerNorm(hidden_dim, eps=1e-12))

    def forward(self, tensor):
        for i in range(self.fcn_layers):
            tensor = tensor + self.ffns[i](tensor)
            tensor = self.layer_norm2[i](tensor)
        return tensor

# 모델 정의
class Sepsis_Pred_Model(nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super(Sepsis_Pred_Model, self).__init__()
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.num_layers = 2
        self.dropout = 0.5
        self.bidirectional = True

        # Linear projection layer
        self.embedding = nn.Linear(input_dim, hidden_dim)
        self.layer_norm_emb = nn.LayerNorm(hidden_dim, eps=1e-12)
        self.fcn = FCN_LN(self.hidden_dim, self.dropout)
        # BiLSTM layers
        self.lstm = nn.LSTM(input_size=hidden_dim,
                            hidden_size=hidden_dim,
                            num_layers=self.num_layers,
                            batch_first=True,
                            dropout=self.dropout,
                            bidirectional=self.bidirectional)

        # Binary classifier layers
        self.classifier = nn.Sequential(
            nn.LayerNorm(hidden_dim * 2 if self.bidirectional else hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim * 2 if self.bidirectional else hidden_dim, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1),
        )

    def forward(self, x):
        x = self.embedding(x)
        x = self.layer_norm_emb(x)
        x = self.fcn(x)
        lstm_out, _ = self.lstm(x)
        x = lstm_out[:,-1]
        output = self.classifier(x)

        return output