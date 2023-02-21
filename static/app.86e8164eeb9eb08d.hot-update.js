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

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var vue_router__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! vue-router */ \"./node_modules/vue-router/dist/vue-router.mjs\");\n\nconst routes = [{\n  path: '/',\n  name: 'Main',\n  component: () => __webpack_require__.e(/*! import() | home */ \"home\").then(__webpack_require__.bind(__webpack_require__, /*! ../views/main/MainView.vue */ \"./src/views/main/MainView.vue\"))\n}, {\n  path: '/detected',\n  name: 'Detected',\n  component: () => __webpack_require__.e(/*! import() | home */ \"home\").then(__webpack_require__.bind(__webpack_require__, /*! ../views/main/DetectedView.vue */ \"./src/views/main/DetectedView.vue\"))\n}, {\n  path: '/detail/patient',\n  name: 'Patient',\n  component: () => __webpack_require__.e(/*! import() | detail */ \"detail\").then(__webpack_require__.bind(__webpack_require__, /*! ../views/patient/PatientView.vue */ \"./src/views/patient/PatientView.vue\"))\n}, {\n  path: '/detail/vital',\n  name: 'Vital',\n  component: () => __webpack_require__.e(/*! import() | detail */ \"detail\").then(__webpack_require__.bind(__webpack_require__, /*! ../views/patient/VitalView.vue */ \"./src/views/patient/VitalView.vue\"))\n}, {\n  path: '/pop/addpatient',\n  name: 'AddPatient',\n  component: () => __webpack_require__.e(/*! import() | pop */ \"pop\").then(__webpack_require__.bind(__webpack_require__, /*! ../views/popups/AddPatient.vue */ \"./src/views/popups/AddPatient.vue\"))\n}, {\n  path: '/pop/addvital',\n  name: 'AddVital',\n  component: () => __webpack_require__.e(/*! import() | pop */ \"pop\").then(__webpack_require__.bind(__webpack_require__, /*! ../views/popups/AddVital.vue */ \"./src/views/popups/AddVital.vue\"))\n}];\nconst router = (0,vue_router__WEBPACK_IMPORTED_MODULE_0__.createRouter)({\n  history: (0,vue_router__WEBPACK_IMPORTED_MODULE_0__.createWebHistory)(\"\"),\n  routes\n});\n/* harmony default export */ __webpack_exports__[\"default\"] = (router);//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvcm91dGVyL2luZGV4LmpzLmpzIiwibWFwcGluZ3MiOiI7O0FBQUE7QUFFQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUdBO0FBQ0E7QUFDQTtBQUNBO0FBRUEiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9zbWhyZC8uL3NyYy9yb3V0ZXIvaW5kZXguanM/NWFhNCJdLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgeyBjcmVhdGVSb3V0ZXIsIGNyZWF0ZVdlYkhpc3RvcnkgfSBmcm9tICd2dWUtcm91dGVyJ1xuXG5jb25zdCByb3V0ZXMgPSBbXG4gIHtcbiAgICBwYXRoOiAnLycsXG4gICAgbmFtZTogJ01haW4nLFxuICAgIGNvbXBvbmVudDogKCkgPT4gaW1wb3J0KC8qIHdlYnBhY2tDaHVua05hbWU6IFwiaG9tZVwiICovICcuLi92aWV3cy9tYWluL01haW5WaWV3LnZ1ZScpXG4gIH0sXG4gIHtcbiAgICBwYXRoOiAnL2RldGVjdGVkJyxcbiAgICBuYW1lOiAnRGV0ZWN0ZWQnLFxuICAgIGNvbXBvbmVudDogKCkgPT4gaW1wb3J0KC8qIHdlYnBhY2tDaHVua05hbWU6IFwiaG9tZVwiLCB3ZWJwYWNrUHJlZmV0Y2g6dHJ1ZSAqLyAnLi4vdmlld3MvbWFpbi9EZXRlY3RlZFZpZXcudnVlJylcbiAgfSxcbiAge1xuICAgIHBhdGg6ICcvZGV0YWlsL3BhdGllbnQnLFxuICAgIG5hbWU6ICdQYXRpZW50JyxcbiAgICBjb21wb25lbnQ6ICgpID0+IGltcG9ydCgvKiB3ZWJwYWNrQ2h1bmtOYW1lOiBcImRldGFpbFwiLCB3ZWJwYWNrUHJlZmV0Y2g6dHJ1ZSAqLyAnLi4vdmlld3MvcGF0aWVudC9QYXRpZW50Vmlldy52dWUnKVxuICB9LFxuICB7XG4gICAgcGF0aDogJy9kZXRhaWwvdml0YWwnLFxuICAgIG5hbWU6ICdWaXRhbCcsXG4gICAgY29tcG9uZW50OiAoKSA9PiBpbXBvcnQoLyogd2VicGFja0NodW5rTmFtZTogXCJkZXRhaWxcIiwgd2VicGFja1ByZWZldGNoOnRydWUgKi8gJy4uL3ZpZXdzL3BhdGllbnQvVml0YWxWaWV3LnZ1ZScpXG4gIH0sXG4gIHtcbiAgICBwYXRoOiAnL3BvcC9hZGRwYXRpZW50JyxcbiAgICBuYW1lOiAnQWRkUGF0aWVudCcsXG4gICAgY29tcG9uZW50OiAoKSA9PiBpbXBvcnQoLyogd2VicGFja0NodW5rTmFtZTogXCJwb3BcIiwgd2VicGFja1ByZWZldGNoOnRydWUgKi8gJy4uL3ZpZXdzL3BvcHVwcy9BZGRQYXRpZW50LnZ1ZScpXG4gIH0sXG4gIHtcbiAgICBwYXRoOiAnL3BvcC9hZGR2aXRhbCcsXG4gICAgbmFtZTogJ0FkZFZpdGFsJyxcbiAgICBjb21wb25lbnQ6ICgpID0+IGltcG9ydCgvKiB3ZWJwYWNrQ2h1bmtOYW1lOiBcInBvcFwiLCB3ZWJwYWNrUHJlZmV0Y2g6dHJ1ZSAqLyAnLi4vdmlld3MvcG9wdXBzL0FkZFZpdGFsLnZ1ZScpXG4gIH1cbl1cblxuY29uc3Qgcm91dGVyID0gY3JlYXRlUm91dGVyKHtcbiAgaGlzdG9yeTogY3JlYXRlV2ViSGlzdG9yeShwcm9jZXNzLmVudi5CQVNFX1VSTCksXG4gIHJvdXRlc1xufSlcblxuZXhwb3J0IGRlZmF1bHQgcm91dGVyXG4iXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///./src/router/index.js\n");

/***/ })

},
/******/ function(__webpack_require__) { // webpackRuntimeModules
/******/ /* webpack/runtime/getFullHash */
/******/ !function() {
/******/ 	__webpack_require__.h = function() { return "e3dc7824ae597117"; }
/******/ }();
/******/ 
/******/ /* webpack/runtime/startup prefetch */
/******/ !function() {
/******/ 	__webpack_require__.O(0, ["app"], function() {
/******/ 		["home","detail","pop"].map(__webpack_require__.E);
/******/ 	}, 5);
/******/ }();
/******/ 
/******/ }
);