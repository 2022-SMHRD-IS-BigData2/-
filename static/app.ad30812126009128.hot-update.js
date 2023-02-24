/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(typeof self !== 'undefined' ? self : this)["webpackHotUpdatesmhrd"]("app",{

/***/ "./src/router/index.js":
/*!*****************************!*\
  !*** ./src/router/index.js ***!
  \*****************************/
/***/ (function(__unused_webpack_module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var vue_router__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! vue-router */ \"./node_modules/vue-router/dist/vue-router.mjs\");\n/* harmony import */ var _views_main_MainView_vue__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../views/main/MainView.vue */ \"./src/views/main/MainView.vue\");\n/* harmony import */ var _views_main_DetectedView_vue__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../views/main/DetectedView.vue */ \"./src/views/main/DetectedView.vue\");\n/* harmony import */ var _views_patient_PatientView_vue__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../views/patient/PatientView.vue */ \"./src/views/patient/PatientView.vue\");\n/* harmony import */ var _views_patient_PatientView_vue__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_views_patient_PatientView_vue__WEBPACK_IMPORTED_MODULE_2__);\n/* harmony import */ var _views_patient_VitalView_vue__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../views/patient/VitalView.vue */ \"./src/views/patient/VitalView.vue\");\n\n\n\n\n\nconst routes = [{\n  path: '/',\n  name: 'MainView',\n  component: _views_main_MainView_vue__WEBPACK_IMPORTED_MODULE_0__[\"default\"]\n}, {\n  path: '/detected',\n  name: 'DetectedView',\n  component: _views_main_DetectedView_vue__WEBPACK_IMPORTED_MODULE_1__[\"default\"]\n}, {\n  path: '/patient',\n  name: 'PatientView',\n  component: (_views_patient_PatientView_vue__WEBPACK_IMPORTED_MODULE_2___default())\n}, {\n  path: '/vital',\n  name: 'VitalView',\n  component: _views_patient_VitalView_vue__WEBPACK_IMPORTED_MODULE_3__[\"default\"]\n}, {\n  path: '/addpatient',\n  name: 'AddPatient',\n  component: () => __webpack_require__.e(/*! import() | home */ \"home\").then(__webpack_require__.bind(__webpack_require__, /*! ../views/popups/AddPatient.vue */ \"./src/views/popups/AddPatient.vue\"))\n}, {\n  path: '/addvital',\n  name: 'AddVital',\n  component: () => __webpack_require__.e(/*! import() | home */ \"home\").then(__webpack_require__.bind(__webpack_require__, /*! ../views/popups/AddVital.vue */ \"./src/views/popups/AddVital.vue\"))\n}, {\n  path: '/getAllPatient',\n  name: 'getAllPatient',\n  component: () => __webpack_require__.e(/*! import() | home */ \"home\").then(__webpack_require__.t.bind(__webpack_require__, /*! ../views/patient/PatientView.vue */ \"./src/views/patient/PatientView.vue\", 23))\n}];\nconst router = (0,vue_router__WEBPACK_IMPORTED_MODULE_4__.createRouter)({\n  history: (0,vue_router__WEBPACK_IMPORTED_MODULE_4__.createWebHistory)(\"\"),\n  routes\n});\n/* harmony default export */ __webpack_exports__[\"default\"] = (router);//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvcm91dGVyL2luZGV4LmpzLmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7QUFBQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBRUE7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUdBO0FBQ0E7QUFDQTtBQUNBO0FBRUEiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9zbWhyZC8uL3NyYy9yb3V0ZXIvaW5kZXguanM/NWFhNCJdLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgeyBjcmVhdGVSb3V0ZXIsIGNyZWF0ZVdlYkhpc3RvcnkgfSBmcm9tICd2dWUtcm91dGVyJ1xyXG5pbXBvcnQgTWFpblZpZXcgZnJvbSAnLi4vdmlld3MvbWFpbi9NYWluVmlldy52dWUnXHJcbmltcG9ydCBEZXRlY3RlZFZpZXcgZnJvbSAnLi4vdmlld3MvbWFpbi9EZXRlY3RlZFZpZXcudnVlJ1xyXG5pbXBvcnQgUGF0aWVudFZpZXcgZnJvbSAnLi4vdmlld3MvcGF0aWVudC9QYXRpZW50Vmlldy52dWUnXHJcbmltcG9ydCBWaXRhbFZpZXcgZnJvbSAnLi4vdmlld3MvcGF0aWVudC9WaXRhbFZpZXcudnVlJ1xyXG5cclxuY29uc3Qgcm91dGVzID0gW1xyXG4gIHtcclxuICAgIHBhdGg6ICcvJyxcclxuICAgIG5hbWU6ICdNYWluVmlldycsXHJcbiAgICBjb21wb25lbnQ6IE1haW5WaWV3XHJcbiAgfSxcclxuICB7XHJcbiAgICBwYXRoOiAnL2RldGVjdGVkJyxcclxuICAgIG5hbWU6ICdEZXRlY3RlZFZpZXcnLFxyXG4gICAgY29tcG9uZW50OiBEZXRlY3RlZFZpZXdcclxuICB9LFxyXG4gIHtcclxuICAgIHBhdGg6ICcvcGF0aWVudCcsXHJcbiAgICBuYW1lOiAnUGF0aWVudFZpZXcnLFxyXG4gICAgY29tcG9uZW50OiBQYXRpZW50Vmlld1xyXG4gIH0sXHJcbiAge1xyXG4gICAgcGF0aDogJy92aXRhbCcsXHJcbiAgICBuYW1lOiAnVml0YWxWaWV3JyxcclxuICAgIGNvbXBvbmVudDogVml0YWxWaWV3XHJcbiAgfSxcclxuICB7XHJcbiAgICBwYXRoOiAnL2FkZHBhdGllbnQnLFxyXG4gICAgbmFtZTogJ0FkZFBhdGllbnQnLFxyXG4gICAgY29tcG9uZW50OiAoKSA9PiBpbXBvcnQoLyogd2VicGFja0NodW5rTmFtZTogXCJob21lXCIgKi8gJy4uL3ZpZXdzL3BvcHVwcy9BZGRQYXRpZW50LnZ1ZScpXHJcbiAgfSxcclxuICB7XHJcbiAgICBwYXRoOiAnL2FkZHZpdGFsJyxcclxuICAgIG5hbWU6ICdBZGRWaXRhbCcsXHJcbiAgICBjb21wb25lbnQ6ICgpID0+IGltcG9ydCgvKiB3ZWJwYWNrQ2h1bmtOYW1lOiBcImhvbWVcIiAqLyAnLi4vdmlld3MvcG9wdXBzL0FkZFZpdGFsLnZ1ZScpXHJcbiAgfSxcclxuICB7XHJcbiAgICBwYXRoOiAnL2dldEFsbFBhdGllbnQnLFxyXG4gICAgbmFtZTogJ2dldEFsbFBhdGllbnQnLFxyXG4gICAgY29tcG9uZW50OiAoKSA9PiBpbXBvcnQoLyogd2VicGFja0NodW5rTmFtZTogXCJob21lXCIgKi8gJy4uL3ZpZXdzL3BhdGllbnQvUGF0aWVudFZpZXcudnVlJylcclxuICB9XHJcbl1cclxuXHJcbmNvbnN0IHJvdXRlciA9IGNyZWF0ZVJvdXRlcih7XHJcbiAgaGlzdG9yeTogY3JlYXRlV2ViSGlzdG9yeShwcm9jZXNzLmVudi5CQVNFX1VSTCksXHJcbiAgcm91dGVzXHJcbn0pXHJcblxyXG5leHBvcnQgZGVmYXVsdCByb3V0ZXJcclxuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///./src/router/index.js\n");

/***/ }),

/***/ "./src/views/patient/PatientView.vue":
/*!*******************************************!*\
  !*** ./src/views/patient/PatientView.vue ***!
  \*******************************************/
/***/ (function() {



/***/ })

},
/******/ function(__webpack_require__) { // webpackRuntimeModules
/******/ /* webpack/runtime/create fake namespace object */
/******/ !function() {
/******/ 	var getProto = Object.getPrototypeOf ? function(obj) { return Object.getPrototypeOf(obj); } : function(obj) { return obj.__proto__; };
/******/ 	var leafPrototypes;
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 16: return value when it's Promise-like
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = this(value);
/******/ 		if(mode & 8) return value;
/******/ 		if(typeof value === 'object' && value) {
/******/ 			if((mode & 4) && value.__esModule) return value;
/******/ 			if((mode & 16) && typeof value.then === 'function') return value;
/******/ 		}
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		var def = {};
/******/ 		leafPrototypes = leafPrototypes || [null, getProto({}), getProto([]), getProto(getProto)];
/******/ 		for(var current = mode & 2 && value; typeof current == 'object' && !~leafPrototypes.indexOf(current); current = getProto(current)) {
/******/ 			Object.getOwnPropertyNames(current).forEach(function(key) { def[key] = function() { return value[key]; }; });
/******/ 		}
/******/ 		def['default'] = function() { return value; };
/******/ 		__webpack_require__.d(ns, def);
/******/ 		return ns;
/******/ 	};
/******/ }();
/******/ 
/******/ /* webpack/runtime/getFullHash */
/******/ !function() {
/******/ 	__webpack_require__.h = function() { return "6626afb4728fc9a0"; }
/******/ }();
/******/ 
/******/ }
);