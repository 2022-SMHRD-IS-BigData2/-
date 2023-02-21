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

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var vue_router__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! vue-router */ \"./node_modules/vue-router/dist/vue-router.mjs\");\n\nconst routes = [{\n  path: '/',\n  name: 'Main',\n  component: () => __webpack_require__.e(/*! import() | about */ \"about\").then(__webpack_require__.bind(__webpack_require__, /*! ../components/main/MainView.vue */ \"./src/components/main/MainView.vue\"))\n}, {\n  path: '/detected',\n  name: 'Detected',\n  component: () => __webpack_require__.e(/*! import() | about */ \"about\").then(__webpack_require__.bind(__webpack_require__, /*! ../components/main/DetectedView.vue */ \"./src/components/main/DetectedView.vue\"))\n}, {\n  path: '/patient',\n  name: 'Patient',\n  component: () => __webpack_require__.e(/*! import() | about */ \"about\").then(__webpack_require__.bind(__webpack_require__, /*! ../components/patient/PatientView.vue */ \"./src/components/patient/PatientView.vue\"))\n}, {\n  path: '/vital',\n  name: 'Vital',\n  component: () => __webpack_require__.e(/*! import() | about */ \"about\").then(__webpack_require__.bind(__webpack_require__, /*! ../components/patient/VitalView.vue */ \"./src/components/patient/VitalView.vue\"))\n}, {\n  path: '/addpatient',\n  name: 'AddPatient',\n  component: () => __webpack_require__.e(/*! import() | about */ \"about\").then(__webpack_require__.bind(__webpack_require__, /*! ../components/popups/AddPatient.vue */ \"./src/components/popups/AddPatient.vue\"))\n}, {\n  path: '/addvital',\n  name: 'AddVital',\n  component: () => __webpack_require__.e(/*! import() | about */ \"about\").then(__webpack_require__.bind(__webpack_require__, /*! ../components/popups/AddVital.vue */ \"./src/components/popups/AddVital.vue\"))\n}];\nconst router = (0,vue_router__WEBPACK_IMPORTED_MODULE_0__.createRouter)({\n  history: (0,vue_router__WEBPACK_IMPORTED_MODULE_0__.createWebHistory)(\"\"),\n  routes\n});\n/* harmony default export */ __webpack_exports__[\"default\"] = (router);//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvcm91dGVyL2luZGV4LmpzLmpzIiwibWFwcGluZ3MiOiI7O0FBQUE7QUFFQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUdBO0FBQ0E7QUFDQTtBQUNBO0FBRUEiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9zbWhyZC8uL3NyYy9yb3V0ZXIvaW5kZXguanM/NWFhNCJdLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgeyBjcmVhdGVSb3V0ZXIsIGNyZWF0ZVdlYkhpc3RvcnkgfSBmcm9tICd2dWUtcm91dGVyJ1xuXG5jb25zdCByb3V0ZXMgPSBbXG4gIHtcbiAgICBwYXRoOiAnLycsXG4gICAgbmFtZTogJ01haW4nLFxuICAgIGNvbXBvbmVudDogKCkgPT4gaW1wb3J0KC8qIHdlYnBhY2tDaHVua05hbWU6IFwiYWJvdXRcIiAqLyAnLi4vY29tcG9uZW50cy9tYWluL01haW5WaWV3LnZ1ZScpXG4gIH0sXG4gIHtcbiAgICBwYXRoOiAnL2RldGVjdGVkJyxcbiAgICBuYW1lOiAnRGV0ZWN0ZWQnLFxuICAgIGNvbXBvbmVudDogKCkgPT4gaW1wb3J0KC8qIHdlYnBhY2tDaHVua05hbWU6IFwiYWJvdXRcIiAqLyAnLi4vY29tcG9uZW50cy9tYWluL0RldGVjdGVkVmlldy52dWUnKVxuICB9LFxuICB7XG4gICAgcGF0aDogJy9wYXRpZW50JyxcbiAgICBuYW1lOiAnUGF0aWVudCcsXG4gICAgY29tcG9uZW50OiAoKSA9PiBpbXBvcnQoLyogd2VicGFja0NodW5rTmFtZTogXCJhYm91dFwiICovICcuLi9jb21wb25lbnRzL3BhdGllbnQvUGF0aWVudFZpZXcudnVlJylcbiAgfSxcbiAge1xuICAgIHBhdGg6ICcvdml0YWwnLFxuICAgIG5hbWU6ICdWaXRhbCcsXG4gICAgY29tcG9uZW50OiAoKSA9PiBpbXBvcnQoLyogd2VicGFja0NodW5rTmFtZTogXCJhYm91dFwiICovICcuLi9jb21wb25lbnRzL3BhdGllbnQvVml0YWxWaWV3LnZ1ZScpXG4gIH0sXG4gIHtcbiAgICBwYXRoOiAnL2FkZHBhdGllbnQnLFxuICAgIG5hbWU6ICdBZGRQYXRpZW50JyxcbiAgICBjb21wb25lbnQ6ICgpID0+IGltcG9ydCgvKiB3ZWJwYWNrQ2h1bmtOYW1lOiBcImFib3V0XCIgKi8gJy4uL2NvbXBvbmVudHMvcG9wdXBzL0FkZFBhdGllbnQudnVlJylcbiAgfSxcbiAge1xuICAgIHBhdGg6ICcvYWRkdml0YWwnLFxuICAgIG5hbWU6ICdBZGRWaXRhbCcsXG4gICAgY29tcG9uZW50OiAoKSA9PiBpbXBvcnQoLyogd2VicGFja0NodW5rTmFtZTogXCJhYm91dFwiICovICcuLi9jb21wb25lbnRzL3BvcHVwcy9BZGRWaXRhbC52dWUnKVxuICB9XG5dXG5cbmNvbnN0IHJvdXRlciA9IGNyZWF0ZVJvdXRlcih7XG4gIGhpc3Rvcnk6IGNyZWF0ZVdlYkhpc3RvcnkocHJvY2Vzcy5lbnYuQkFTRV9VUkwpLFxuICByb3V0ZXNcbn0pXG5cbmV4cG9ydCBkZWZhdWx0IHJvdXRlclxuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///./src/router/index.js\n");

/***/ })

},
/******/ function(__webpack_require__) { // webpackRuntimeModules
/******/ /* webpack/runtime/getFullHash */
/******/ !function() {
/******/ 	__webpack_require__.h = function() { return "253f6c25d240f706"; }
/******/ }();
/******/ 
/******/ }
);