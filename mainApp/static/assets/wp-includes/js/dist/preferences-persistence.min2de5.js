/*! This file is auto-generated */
!function(){"use strict";var e={n:function(n){var r=n&&n.__esModule?function(){return n.default}:function(){return n};return e.d(r,{a:r}),r},d:function(n,r){for(var o in r)e.o(r,o)&&!e.o(n,o)&&Object.defineProperty(n,o,{enumerable:!0,get:r[o]})},o:function(e,n){return Object.prototype.hasOwnProperty.call(e,n)},r:function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})}},n={};e.r(n),e.d(n,{__unstableCreatePersistenceLayer:function(){return m},create:function(){return c}});var r=window.wp.apiFetch,o=e.n(r);function t(e,n){let r,o;return async function(){for(var t=arguments.length,l=new Array(t),i=0;i<t;i++)l[i]=arguments[i];return o||r?(o&&await o,r&&(clearTimeout(r),r=null),new Promise(((t,i)=>{r=setTimeout((()=>{o=e(...l).then((function(){t(...arguments)})).catch((e=>{i(e)})).finally((()=>{o=null,r=null}))}),n)}))):new Promise(((n,r)=>{o=e(...l).then((function(){n(...arguments)})).catch((e=>{r(e)})).finally((()=>{o=null}))}))}}const l={},i=window.localStorage;function c(){let{preloadedData:e,localStorageRestoreKey:n="WP_PREFERENCES_RESTORE_DATA",requestDebounceMS:r=2500}=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},c=e;const u=t(o(),r);async function d(){var e;if(c)return c;const r=await o()({path:"/wp/v2/users/me?context=edit"}),t=null==r||null===(e=r.meta)||void 0===e?void 0:e.persisted_preferences,u=JSON.parse(i.getItem(n)),d=Date.parse(null==t?void 0:t._modified)||0,s=Date.parse(null==u?void 0:u._modified)||0;return c=t&&d>=s?t:u||l,c}function s(e){const r={...e,_modified:(new Date).toISOString()};c=r,i.setItem(n,JSON.stringify(r)),u({path:"/wp/v2/users/me",method:"PUT",keepalive:!0,data:{meta:{persisted_preferences:r}}}).catch((()=>{}))}return{get:d,set:s}}function u(e,n){var r,o,t,l,i,c;const u="core/preferences",d="core/interface",s=null==e||null===(r=e["core/interface"])||void 0===r||null===(o=r.preferences)||void 0===o||null===(t=o.features)||void 0===t?void 0:t[n],a=null==e||null===(l=e[n])||void 0===l||null===(i=l.preferences)||void 0===i?void 0:i.features,f=s||a;if(!f)return e;const v=null==e||null===(c=e["core/preferences"])||void 0===c?void 0:c.preferences;if(null!=v&&v[n])return e;let p,m;if(s){var y,w;p={[d]:{...null==e?void 0:e["core/interface"],preferences:{features:{...null==e||null===(y=e["core/interface"])||void 0===y||null===(w=y.preferences)||void 0===w?void 0:w.features,[n]:void 0}}}}}if(a){var b;m={[n]:{...null==e?void 0:e[n],preferences:{...null==e||null===(b=e[n])||void 0===b?void 0:b.preferences,features:void 0}}}}return{...e,[u]:{preferences:{...v,[n]:f}},...p,...m}}const d=e=>e;function s(e,n,r){var o,t,l,i,c,u,s,a,f;let{from:v,to:p}=n,m=arguments.length>3&&void 0!==arguments[3]?arguments[3]:d;const y="core/preferences",w=null==e||null===(o=e[v])||void 0===o||null===(t=o.preferences)||void 0===t?void 0:t[r];if(void 0===w)return e;const b=null==e||null===(l=e[y])||void 0===l||null===(i=l.preferences)||void 0===i||null===(c=i[p])||void 0===c?void 0:c[r];if(b)return e;const S=null==e||null===(u=e[y])||void 0===u?void 0:u.preferences,g=null==e||null===(s=e[y])||void 0===s||null===(a=s.preferences)||void 0===a?void 0:a[p],_=null==e?void 0:e[v],h=null==e||null===(f=e[v])||void 0===f?void 0:f.preferences,P=m({[r]:w});return{...e,[y]:{preferences:{...S,[p]:{...g,...P}}},[v]:{..._,preferences:{...h,[r]:void 0}}}}function a(e){var n;const r=null!==(n=null==e?void 0:e.panels)&&void 0!==n?n:{};return Object.keys(r).reduce(((e,n)=>{const o=r[n];return!1===(null==o?void 0:o.enabled)&&e.inactivePanels.push(n),!0===(null==o?void 0:o.opened)&&e.openPanels.push(n),e}),{inactivePanels:[],openPanels:[]})}function f(e){var n,r;if(e)return e=u(e,"core/edit-widgets"),e=u(e,"core/customize-widgets"),e=u(e,"core/edit-post"),e=s(e=function(e){var n,r,o,t,l,i,c;const u="core/interface",d="core/preferences",s=null==e||null===(n=e["core/interface"])||void 0===n?void 0:n.enableItems;if(!s)return e;const a=null!==(r=null==e||null===(o=e["core/preferences"])||void 0===o?void 0:o.preferences)&&void 0!==r?r:{},f=null!==(t=null==s||null===(l=s.singleEnableItems)||void 0===l?void 0:l.complementaryArea)&&void 0!==t?t:{},v=Object.keys(f).reduce(((e,n)=>{var r;const o=f[n];return null!=e&&null!==(r=e[n])&&void 0!==r&&r.complementaryArea?e:{...e,[n]:{...e[n],complementaryArea:o}}}),a),p=null!==(i=null==s||null===(c=s.multipleEnableItems)||void 0===c?void 0:c.pinnedItems)&&void 0!==i?i:{},m=Object.keys(p).reduce(((e,n)=>{var r;const o=p[n];return null!=e&&null!==(r=e[n])&&void 0!==r&&r.pinnedItems?e:{...e,[n]:{...e[n],pinnedItems:o}}}),v),y=e["core/interface"];return{...e,[d]:{preferences:m},[u]:{...y,enableItems:void 0}}}(e=function(e){var n,r;const o="core/interface",t="core/preferences",l=null==e||null===(n=e["core/interface"])||void 0===n||null===(r=n.preferences)||void 0===r?void 0:r.features,i=l?Object.keys(l):[];return null!=i&&i.length?i.reduce((function(e,n){var r,i,c,u,d;if(n.startsWith("core"))return e;const s=null==l?void 0:l[n];if(!s)return e;if(null==e||null===(r=e["core/preferences"])||void 0===r||null===(i=r.preferences)||void 0===i?void 0:i[n])return e;const a=null==e||null===(c=e["core/preferences"])||void 0===c?void 0:c.preferences,f=null==e?void 0:e["core/interface"],v=null==e||null===(u=e["core/interface"])||void 0===u||null===(d=u.preferences)||void 0===d?void 0:d.features;return{...e,[t]:{preferences:{...a,[n]:s}},[o]:{...f,preferences:{features:{...v,[n]:void 0}}}}}),e):e}(e=u(e,"core/edit-site"))),{from:"core/edit-post",to:"core/edit-post"},"hiddenBlockTypes"),e=s(e,{from:"core/edit-post",to:"core/edit-post"},"editorMode"),e=s(e,{from:"core/edit-post",to:"core/edit-post"},"preferredStyleVariations"),e=s(e,{from:"core/edit-post",to:"core/edit-post"},"panels",a),e=s(e,{from:"core/editor",to:"core/edit-post"},"isPublishSidebarEnabled"),null===(n=e=s(e,{from:"core/edit-site",to:"core/edit-site"},"editorMode"))||void 0===n||null===(r=n["core/preferences"])||void 0===r?void 0:r.preferences}function v(e){const n=function(e){const n=`WP_DATA_USER_${e}`,r=window.localStorage.getItem(n);return JSON.parse(r)}(e);return f(n)}function p(e){return n=e,Object.keys(n).reduce(((e,r)=>{const o=n[r];if(null!=o&&o.complementaryArea){const n={...o};return delete n.complementaryArea,n.isComplementaryAreaVisible=!0,e[r]=n,e}return e}),n);var n}function m(e,n){const r=`WP_PREFERENCES_USER_${n}`,o=JSON.parse(window.localStorage.getItem(r)),t=Date.parse(e&&e._modified)||0,l=Date.parse(o&&o._modified)||0;let i;return i=e&&t>=l?p(e):o?p(o):v(n),c({preloadedData:i,localStorageRestoreKey:r})}(window.wp=window.wp||{}).preferencesPersistence=n}();