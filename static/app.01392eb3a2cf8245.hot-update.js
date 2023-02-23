"use strict";
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

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var vue_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! vue-router */ \"./node_modules/vue-router/dist/vue-router.mjs\");\n/* harmony import */ var _views_main_MainView_vue__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../views/main/MainView.vue */ \"./src/views/main/MainView.vue\");\n\n\nconst routes = [{\n  path: '/',\n  name: 'MainView',\n  component: _views_main_MainView_vue__WEBPACK_IMPORTED_MODULE_0__[\"default\"]\n}, {\n  path: '/detected',\n  name: 'DetectedView',\n  component: () => __webpack_require__.e(/*! import() | home */ \"home\").then(__webpack_require__.bind(__webpack_require__, /*! ../views/main/DetectedView.vue */ \"./src/views/main/DetectedView.vue\"))\n}, {\n  path: '/patient',\n  name: 'PatientView',\n  component: () => __webpack_require__.e(/*! import() | home */ \"home\").then(__webpack_require__.bind(__webpack_require__, /*! ../views/patient/PatientView.vue */ \"./src/views/patient/PatientView.vue\"))\n}, {\n  path: '/vital',\n  name: 'VitalView',\n  component: () => __webpack_require__.e(/*! import() | home */ \"home\").then(__webpack_require__.bind(__webpack_require__, /*! ../views/patient/VitalView.vue */ \"./src/views/patient/VitalView.vue\"))\n}, {\n  path: '/addpatient',\n  name: 'AddPatient',\n  component: () => __webpack_require__.e(/*! import() | home */ \"home\").then(__webpack_require__.bind(__webpack_require__, /*! ../views/popups/AddPatient.vue */ \"./src/views/popups/AddPatient.vue\"))\n}, {\n  path: '/addvital',\n  name: 'AddVital',\n  component: () => __webpack_require__.e(/*! import() | home */ \"home\").then(__webpack_require__.bind(__webpack_require__, /*! ../views/popups/AddVital.vue */ \"./src/views/popups/AddVital.vue\"))\n}\n// {\n//   path: '/getAllPatient',\n//   name: 'getAllPatient',\n//   component : PatientView\n// }\n];\n\nconst router = (0,vue_router__WEBPACK_IMPORTED_MODULE_1__.createRouter)({\n  history: (0,vue_router__WEBPACK_IMPORTED_MODULE_1__.createWebHistory)(\"\"),\n  routes\n});\n/* harmony default export */ __webpack_exports__[\"default\"] = (router);//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvcm91dGVyL2luZGV4LmpzLmpzIiwibWFwcGluZ3MiOiI7OztBQUFBO0FBQ0E7QUFFQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFBQTs7QUFHQTtBQUNBO0FBQ0E7QUFDQTtBQUVBIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vc21ocmQvLi9zcmMvcm91dGVyL2luZGV4LmpzPzVhYTQiXSwic291cmNlc0NvbnRlbnQiOlsiaW1wb3J0IHsgY3JlYXRlUm91dGVyLCBjcmVhdGVXZWJIaXN0b3J5IH0gZnJvbSAndnVlLXJvdXRlcidcclxuaW1wb3J0IE1haW5WaWV3IGZyb20gJy4uL3ZpZXdzL21haW4vTWFpblZpZXcudnVlJ1xyXG5cclxuY29uc3Qgcm91dGVzID0gW1xyXG4gIHtcclxuICAgIHBhdGg6ICcvJyxcclxuICAgIG5hbWU6ICdNYWluVmlldycsXHJcbiAgICBjb21wb25lbnQ6IE1haW5WaWV3XHJcbiAgfSxcclxuICB7XHJcbiAgICBwYXRoOiAnL2RldGVjdGVkJyxcclxuICAgIG5hbWU6ICdEZXRlY3RlZFZpZXcnLFxyXG4gICAgY29tcG9uZW50OiAoKSA9PiBpbXBvcnQoLyogd2VicGFja0NodW5rTmFtZTogXCJob21lXCIsIHdlYnBhY2tQcmVmZXRjaDp0cnVlICovICcuLi92aWV3cy9tYWluL0RldGVjdGVkVmlldy52dWUnKVxyXG4gIH0sXHJcbiAge1xyXG4gICAgcGF0aDogJy9wYXRpZW50JyxcclxuICAgIG5hbWU6ICdQYXRpZW50VmlldycsXHJcbiAgICBjb21wb25lbnQ6ICgpID0+IGltcG9ydCgvKiB3ZWJwYWNrQ2h1bmtOYW1lOiBcImhvbWVcIiwgd2VicGFja1ByZWZldGNoOnRydWUgKi8gJy4uL3ZpZXdzL3BhdGllbnQvUGF0aWVudFZpZXcudnVlJylcclxuICB9LFxyXG4gIHtcclxuICAgIHBhdGg6ICcvdml0YWwnLFxyXG4gICAgbmFtZTogJ1ZpdGFsVmlldycsXHJcbiAgICBjb21wb25lbnQ6ICgpID0+IGltcG9ydCgvKiB3ZWJwYWNrQ2h1bmtOYW1lOiBcImhvbWVcIiwgd2VicGFja1ByZWZldGNoOnRydWUgKi8gJy4uL3ZpZXdzL3BhdGllbnQvVml0YWxWaWV3LnZ1ZScpXHJcbiAgfSxcclxuICB7XHJcbiAgICBwYXRoOiAnL2FkZHBhdGllbnQnLFxyXG4gICAgbmFtZTogJ0FkZFBhdGllbnQnLFxyXG4gICAgY29tcG9uZW50OiAoKSA9PiBpbXBvcnQoLyogd2VicGFja0NodW5rTmFtZTogXCJob21lXCIgKi8gJy4uL3ZpZXdzL3BvcHVwcy9BZGRQYXRpZW50LnZ1ZScpXHJcbiAgfSxcclxuICB7XHJcbiAgICBwYXRoOiAnL2FkZHZpdGFsJyxcclxuICAgIG5hbWU6ICdBZGRWaXRhbCcsXHJcbiAgICBjb21wb25lbnQ6ICgpID0+IGltcG9ydCgvKiB3ZWJwYWNrQ2h1bmtOYW1lOiBcImhvbWVcIiAqLyAnLi4vdmlld3MvcG9wdXBzL0FkZFZpdGFsLnZ1ZScpXHJcbiAgfSxcclxuICAvLyB7XHJcbiAgLy8gICBwYXRoOiAnL2dldEFsbFBhdGllbnQnLFxyXG4gIC8vICAgbmFtZTogJ2dldEFsbFBhdGllbnQnLFxyXG4gIC8vICAgY29tcG9uZW50IDogUGF0aWVudFZpZXdcclxuICAvLyB9XHJcbl1cclxuXHJcbmNvbnN0IHJvdXRlciA9IGNyZWF0ZVJvdXRlcih7XHJcbiAgaGlzdG9yeTogY3JlYXRlV2ViSGlzdG9yeShwcm9jZXNzLmVudi5CQVNFX1VSTCksXHJcbiAgcm91dGVzXHJcbn0pXHJcblxyXG5leHBvcnQgZGVmYXVsdCByb3V0ZXJcclxuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///./src/router/index.js\n");

/***/ })

},
/******/ function(__webpack_require__) { // webpackRuntimeModules
/******/ /* webpack/runtime/getFullHash */
/******/ !function() {
/******/ 	__webpack_require__.h = function() { return "e6641d245dfc0474"; }
/******/ }();
/******/ 
/******/ }
);