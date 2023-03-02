import { createStore } from 'vuex';

export default createStore({
  state: {
    searchQuery: '',
  },
  getters: {},
  mutations: {
    // 데이터 가져오기
    setSearchQuery(state, query) {
      state.searchQuery = query;
    },
  },
  actions: {
    // 데이터 가져오기
    setSearchQuery({ commit }, query) {
      commit('setSearchQuery', query);
    },
    },
  modules: {},
});
