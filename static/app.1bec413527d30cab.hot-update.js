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

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var vue_router__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! vue-router */ \"./node_modules/vue-router/dist/vue-router.mjs\");\n\nconst routes = [{\n  path: '/',\n  name: 'MainView',\n  component: () => __webpack_require__.e(/*! import() | home */ \"home\").then(__webpack_require__.bind(__webpack_require__, /*! ../views/main/MainView.vue */ \"./src/views/main/MainView.vue\"))\n}, {\n  path: '/detected',\n  name: 'DetectedView',\n  component: () => __webpack_require__.e(/*! import() | home */ \"home\").then(__webpack_require__.bind(__webpack_require__, /*! ../views/main/DetectedView.vue */ \"./src/views/main/DetectedView.vue\"))\n}, {\n  path: '/patient',\n  name: 'PatientView',\n  component: () => __webpack_require__.e(/*! import() | home */ \"home\").then(__webpack_require__.bind(__webpack_require__, /*! ../views/patient/PatientView.vue */ \"./src/views/patient/PatientView.vue\"))\n}, {\n  path: '/vital',\n  name: 'VitalView',\n  component: () => __webpack_require__.e(/*! import() | home */ \"home\").then(__webpack_require__.bind(__webpack_require__, /*! ../views/patient/VitalView.vue */ \"./src/views/patient/VitalView.vue\"))\n}, {\n  path: '/addpatient',\n  name: 'AddPatient',\n  component: () => __webpack_require__.e(/*! import() | home */ \"home\").then(__webpack_require__.bind(__webpack_require__, /*! ../views/popups/AddPatient.vue */ \"./src/views/popups/AddPatient.vue\"))\n}, {\n  path: '/addvital',\n  name: 'AddVital',\n  component: () => __webpack_require__.e(/*! import() | home */ \"home\").then(__webpack_require__.bind(__webpack_require__, /*! ../views/popups/AddVital.vue */ \"./src/views/popups/AddVital.vue\"))\n}];\nconst router = (0,vue_router__WEBPACK_IMPORTED_MODULE_0__.createRouter)({\n  history: (0,vue_router__WEBPACK_IMPORTED_MODULE_0__.createWebHistory)(\"\"),\n  routes\n});\n/* harmony default export */ __webpack_exports__[\"default\"] = (router);//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvcm91dGVyL2luZGV4LmpzLmpzIiwibWFwcGluZ3MiOiI7O0FBQUE7QUFFQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUdBO0FBQ0E7QUFDQTtBQUNBO0FBRUEiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9zbWhyZC8uL3NyYy9yb3V0ZXIvaW5kZXguanM/NWFhNCJdLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgeyBjcmVhdGVSb3V0ZXIsIGNyZWF0ZVdlYkhpc3RvcnkgfSBmcm9tICd2dWUtcm91dGVyJ1xuXG5jb25zdCByb3V0ZXMgPSBbXG4gIHtcbiAgICBwYXRoOiAnLycsXG4gICAgbmFtZTogJ01haW5WaWV3JyxcbiAgICBjb21wb25lbnQ6ICgpID0+IGltcG9ydCgvKiB3ZWJwYWNrQ2h1bmtOYW1lOiBcImhvbWVcIiAqLyAnLi4vdmlld3MvbWFpbi9NYWluVmlldy52dWUnKVxuICB9LFxuICB7XG4gICAgcGF0aDogJy9kZXRlY3RlZCcsXG4gICAgbmFtZTogJ0RldGVjdGVkVmlldycsXG4gICAgY29tcG9uZW50OiAoKSA9PiBpbXBvcnQoLyogd2VicGFja0NodW5rTmFtZTogXCJob21lXCIsIHdlYnBhY2tQcmVmZXRjaDp0cnVlICovICcuLi92aWV3cy9tYWluL0RldGVjdGVkVmlldy52dWUnKVxuICB9LFxuICB7XG4gICAgcGF0aDogJy9wYXRpZW50JyxcbiAgICBuYW1lOiAnUGF0aWVudFZpZXcnLFxuICAgIGNvbXBvbmVudDogKCkgPT4gaW1wb3J0KC8qIHdlYnBhY2tDaHVua05hbWU6IFwiaG9tZVwiLCB3ZWJwYWNrUHJlZmV0Y2g6dHJ1ZSAqLyAnLi4vdmlld3MvcGF0aWVudC9QYXRpZW50Vmlldy52dWUnKVxuICB9LFxuICB7XG4gICAgcGF0aDogJy92aXRhbCcsXG4gICAgbmFtZTogJ1ZpdGFsVmlldycsXG4gICAgY29tcG9uZW50OiAoKSA9PiBpbXBvcnQoLyogd2VicGFja0NodW5rTmFtZTogXCJob21lXCIsIHdlYnBhY2tQcmVmZXRjaDp0cnVlICovICcuLi92aWV3cy9wYXRpZW50L1ZpdGFsVmlldy52dWUnKVxuICB9LFxuICB7XG4gICAgcGF0aDogJy9hZGRwYXRpZW50JyxcbiAgICBuYW1lOiAnQWRkUGF0aWVudCcsXG4gICAgY29tcG9uZW50OiAoKSA9PiBpbXBvcnQoLyogd2VicGFja0NodW5rTmFtZTogXCJob21lXCIgKi8gJy4uL3ZpZXdzL3BvcHVwcy9BZGRQYXRpZW50LnZ1ZScpXG4gIH0sXG4gIHtcbiAgICBwYXRoOiAnL2FkZHZpdGFsJyxcbiAgICBuYW1lOiAnQWRkVml0YWwnLFxuICAgIGNvbXBvbmVudDogKCkgPT4gaW1wb3J0KC8qIHdlYnBhY2tDaHVua05hbWU6IFwiaG9tZVwiICovICcuLi92aWV3cy9wb3B1cHMvQWRkVml0YWwudnVlJylcbiAgfVxuXVxuXG5jb25zdCByb3V0ZXIgPSBjcmVhdGVSb3V0ZXIoe1xuICBoaXN0b3J5OiBjcmVhdGVXZWJIaXN0b3J5KHByb2Nlc3MuZW52LkJBU0VfVVJMKSxcbiAgcm91dGVzXG59KVxuXG5leHBvcnQgZGVmYXVsdCByb3V0ZXJcbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///./src/router/index.js\n");

/***/ })

},
/******/ function(__webpack_require__) { // webpackRuntimeModules
/******/ /* webpack/runtime/getFullHash */
/******/ !function() {
/******/ 	__webpack_require__.h = function() { return "09d613d8f5a0b184"; }
/******/ }();
/******/ 
/******/ /* webpack/runtime/startup prefetch */
/******/ !function() {
/******/ 	__webpack_require__.O(0, ["app"], function() {
/******/ 		__webpack_require__.E("home");
/******/ 	}, 5);
/******/ }();
/******/ 
/******/ }
);