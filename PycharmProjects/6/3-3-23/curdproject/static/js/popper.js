/*
 Copyright (C) Federico Zivolo 2017
 Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).
 */for(var e='undefined'!=typeof window&&'undefined'!=typeof document,t=['Edge','Trident','Firefox'],o=0,n=0;n<t.length;n+=1)if(e&&0<=navigator.userAgent.indexOf(t[n])){o=1;break}function i(e){var t=!1;return function(){t||(t=!0,window.Promise.resolve().then(function(){t=!1,e()}))}}function r(e){var t=!1;return function(){t||(t=!0,setTimeout(function(){t=!1,e()},o))}}var p=e&&window.Promise,s=p?i:r;function d(e){return e&&'[object Function]'==={}.toString.call(e)}function a(e,t){if(1!==e.nodeType)return[];var o=getComputedStyle(e,null);return t?o[t]:o}function l(e){return'HTML'===e.nodeName?e:e.parentNode||e.host}function f(e){if(!e)return document.body;switch(e.nodeName){case'HTML':case'BODY':return e.ownerDocument.body;case'#document':return e.body;}var t=a(e),o=t.overflow,i=t.overflowX,n=t.overflowY;return /(auto|scroll)/.test(o+n+i)?e:f(l(e))}function m(e){var t=e&&e.offsetParent,o=t&&t.nodeName;return o&&'BODY'!==o&&'HTML'!==o?-1!==['TD','TABLE'].indexOf(t.nodeName)&&'static'===a(t,'position')?m(t):t:e?e.ownerDocument.documentElement:document.documentElement}function h(e){var t=e.nodeName;return'BODY'!==t&&('HTML'===t||m(e.firstElementChild)===e)}function c(e){return null===e.parentNode?e:c(e.parentNode)}function g(e,t){if(!e||!e.nodeType||!t||!t.nodeType)return document.documentElement;var o=e.compareDocumentPosition(t)&Node.DOCUMENT_POSITION_FOLLOWING,i=o?e:t,n=o?t:e,r=document.createRange();r.setStart(i,0),r.setEnd(n,0);var p=r.commonAncestorContainer;if(e!==p&&t!==p||i.contains(n))return h(p)?p:m(p);var s=c(e);return s.host?g(s.host,t):g(e,c(t).host)}function u(e){var t=1<arguments.length&&arguments[1]!==void 0?arguments[1]:'top',o='top'===t?'scrollTop':'scrollLeft',i=e.nodeName;if('BODY'===i||'HTML'===i){var n=e.ownerDocument.documentElement,r=e.ownerDocument.scrollingElement||n;return r[o]}return e[o]}function b(e,t){var o=2<arguments.length&&void 0!==arguments[2]&&arguments[2],i=u(t,'top'),n=u(t,'left'),r=o?-1:1;return e.top+=i*r,e.bottom+=i*r,e.left+=n*r,e.right+=n*r,e}function w(e,t){var o='x'===t?'Left':'Top',i='Left'==o?'Right':'Bottom';return parseFloat(e['border'+o+'Width'],10)+parseFloat(e['border'+i+'Width'],10)}var y,E=function(){return void 0==y&&(y=-1!==navigator.appVersion.indexOf('MSIE 10')),y};function v(e,t,o,i){return Math.max(t['offset'+e],t['scroll'+e],o['client'+e],o['offset'+e],o['scroll'+e],E()?o['offset'+e]+i['margin'+('Height'===e?'Top':'Left')]+i['margin'+('Height'===e?'Bottom':'Right')]:0)}function O(){var e=document.body,t=document.documentElement,o=E()&&getComputedStyle(t);return{height:v('Height',e,t,o),width:v('Width',e,t,o)}}var x=function(e,t){if(!(e instanceof t))throw new TypeError('Cannot call a class as a function')},L=function(){function e(e,t){for(var o,n=0;n<t.length;n++)o=t[n],o.enumerable=o.enumerable||!1,o.configurable=!0,'value'in o&&(o.writable=!0),Object.defineProperty(e,o.key,o)}return function(t,o,i){return o&&e(t.prototype,o),i&&e(t,i),t}}(),S=function(e,t,o){return t in e?Object.defineProperty(e,t,{value:o,enumerable:!0,configurable:!0,writable:!0}):e[t]=o,e},T=Object.assign||function(e){for(var t,o=1;o<arguments.length;o++)for(var i in t=arguments[o],t)Object.prototype.hasOwnProperty.call(t,i)&&(e[i]=t[i]);return e};function D(e){return T({},e,{right:e.left+e.width,bottom:e.top+e.height})}function N(e){var t={};if(E())try{t=e.getBoundingClientRect();var o=u(e,'top'),i=u(e,'left');t.top+=o,t.left+=i,t.bottom+=o,t.right+=i}catch(e){}else t=e.getBoundingClientRect();var n={left:t.left,top:t.top,width:t.right-t.left,height:t.bottom-t.top},r='HTML'===e.nodeName?O():{},p=r.width||e.clientWidth||n.right-n.left,s=r.height||e.clientHeight||n.bottom-n.top,d=e.offsetWidth-p,l=e.offsetHeight-s;if(d||l){var f=a(e);d-=w(f,'x'),l-=w(f,'y'),n.width-=d,n.height-=l}return D(n)}function C(e,t){var o=E(),i='HTML'===t.nodeName,n=N(e),r=N(t),p=f(e),s=a(t),d=parseFloat(s.borderTopWidth,10),l=parseFloat(s.borderLeftWidth,10),m=D({top:n.top-r.top-d,left:n.left-r.left-l,width:n.width,height:n.height});if(m.marginTop=0,m.marginLeft=0,!o&&i){var h=parseFloat(s.marginTop,10),c=parseFloat(s.marginLeft,10);m.top-=d-h,m.bottom-=d-h,m.left-=l-c,m.right-=l-c,m.marginTop=h,m.marginLeft=c}return(o?t.contains(p):t===p&&'BODY'!==p.nodeName)&&(m=b(m,t)),m}function k(e){var t=Math.max,o=e.ownerDocument.documentElement,i=C(e,o),n=t(o.clientWidth,window.innerWidth||0),r=t(o.clientHeight,window.innerHeight||0),p=u(o),s=u(o,'left'),d={top:p-i.top+i.marginTop,left:s-i.left+i.marginLeft,width:n,height:r};return D(d)}function W(e){var t=e.nodeName;return'BODY'===t||'HTML'===t?!1:!('fixed'!==a(e,'position'))||W(l(e))}function P(e,t,o,i){var n={top:0,left:0},r=g(e,t);if('viewport'===i)n=k(r);else{var p;'scrollParent'===i?(p=f(l(t)),'BODY'===p.nodeName&&(p=e.ownerDocument.documentElement)):'window'===i?p=e.ownerDocument.documentElement:p=i;var s=C(p,r);if('HTML'===p.nodeName&&!W(r)){var d=O(),a=d.height,m=d.width;n.top+=s.top-s.marginTop,n.bottom=a+s.top,n.left+=s.left-s.marginLeft,n.right=m+s.left}else n=s}return n.left+=o,n.top+=o,n.right-=o,n.bottom-=o,n}function B(e){var t=e.width,o=e.height;return t*o}function H(e,t,o,i,n){var r=5<arguments.length&&arguments[5]!==void 0?arguments[5]:0;if(-1===e.indexOf('auto'))return e;var p=P(o,i,r,n),s={top:{width:p.width,height:t.top-p.top},right:{width:p.right-t.right,height:p.height},bottom:{width:p.width,height:p.bottom-t.bottom},left:{width:t.left-p.left,height:p.height}},d=Object.keys(s).map(function(e){return T({key:e},s[e],{area:B(s[e])})}).sort(function(e,t){return t.area-e.area}),a=d.filter(function(e){var t=e.width,i=e.height;return t>=o.clientWidth&&i>=o.clientHeight}),l=0<a.length?a[0].key:d[0].key,f=e.split('-')[1];return l+(f?'-'+f:'')}function A(e,t,o){var i=g(t,o);return C(o,i)}function I(e){var t=getComputedStyle(e),o=parseFloat(t.marginTop)+parseFloat(t.marginBottom),i=parseFloat(t.marginLeft)+parseFloat(t.marginRight),n={width:e.offsetWidth+i,height:e.offsetHeight+o};return n}function M(e){var t={left:'right',right:'left',bottom:'top',top:'bottom'};return e.replace(/left|right|bottom|top/g,function(e){return t[e]})}function R(e,t,o){o=o.split('-')[0];var i=I(e),n={width:i.width,height:i.height},r=-1!==['right','left'].indexOf(o),p=r?'top':'left',s=r?'left':'top',d=r?'height':'width',a=r?'width':'height';return n[p]=t[p]+t[d]/2-i[d]/2,n[s]=o===s?t[s]-i[a]:t[M(s)],n}function U(e,t){return Array.prototype.find?e.find(t):e.filter(t)[0]}function Y(e,t,o){if(Array.prototype.findIndex)return e.findIndex(function(e){return e[t]===o});var i=U(e,function(e){return e[t]===o});return e.indexOf(i)}function F(e,t,o){var i=void 0===o?e:e.slice(0,Y(e,'name',o));return i.forEach(function(e){e['function']&&console.warn('`modifier.function` is deprecated, use `modifier.fn`!');var o=e['function']||e.fn;e.enabled&&d(o)&&(t.offsets.popper=D(t.offsets.popper),t.offsets.reference=D(t.offsets.reference),t=o(t,e))}),t}function K(){if(!this.state.isDestroyed){var e={instance:this,styles:{},arrowStyles:{},attributes:{},flipped:!1,offsets:{}};e.offsets.reference=A(this.state,this.popper,this.reference),e.placement=H(this.options.placement,e.offsets.reference,this.popper,this.reference,this.options.modifiers.flip.boundariesElement,this.options.modifiers.flip.padding),e.originalPlacement=e.placement,e.offsets.popper=R(this.popper,e.offsets.reference,e.placement),e.offsets.popper.position='absolute',e=F(this.modifiers,e),this.state.isCreated?this.options.onUpdate(e):(this.state.isCreated=!0,this.options.onCreate(e))}}function j(e,t){return e.some(function(e){var o=e.name,i=e.enabled;return i&&o===t})}function q(e){for(var t=[!1,'ms','Webkit','Moz','O'],o=e.charAt(0).toUpperCase()+e.slice(1),n=0;n<t.length-1;n++){var i=t[n],r=i?''+i+o:e;if('undefined'!=typeof document.body.style[r])return r}return null}function V(){return this.state.isDestroyed=!0,j(this.modifiers,'applyStyle')&&(this.popper.removeAttribute('x-placement'),this.popper.style.left='',this.popper.style.position='',this.popper.style.top='',this.popper.style[q('transform')]=''),this.disableEventListeners(),this.options.removeOnDestroy&&this.popper.parentNode.removeChild(this.popper),this}function z(e){var t=e.ownerDocument;return t?t.defaultView:window}function G(e,t,o,i){var n='BODY'===e.nodeName,r=n?e.ownerDocument.defaultView:e;r.addEventListener(t,o,{passive:!0}),n||G(f(r.parentNode),t,o,i),i.push(r)}function _(e,t,o,i){o.updateBound=i,z(e).addEventListener('resize',o.updateBound,{passive:!0});var n=f(e);return G(n,'scroll',o.updateBound,o.scrollParents),o.scrollElement=n,o.eventsEnabled=!0,o}function X(){this.state.eventsEnabled||(this.state=_(this.reference,this.options,this.state,this.scheduleUpdate))}function J(e,t){return z(e).removeEventListener('resize',t.updateBound),t.scrollParents.forEach(function(e){e.removeEventListener('scroll',t.updateBound)}),t.updateBound=null,t.scrollParents=[],t.scrollElement=null,t.eventsEnabled=!1,t}function Q(){this.state.eventsEnabled&&(cancelAnimationFrame(this.scheduleUpdate),this.state=J(this.reference,this.state))}function Z(e){return''!==e&&!isNaN(parseFloat(e))&&isFinite(e)}function $(e,t){Object.keys(t).forEach(function(o){var i='';-1!==['width','height','top','right','bottom','left'].indexOf(o)&&Z(t[o])&&(i='px'),e.style[o]=t[o]+i})}function ee(e,t){Object.keys(t).forEach(function(o){var i=t[o];!1===i?e.removeAttribute(o):e.setAttribute(o,t[o])})}function te(e){return $(e.instance.popper,e.styles),ee(e.instance.popper,e.attributes),e.arrowElement&&Object.keys(e.arrowStyles).length&&$(e.arrowElement,e.arrowStyles),e}function oe(e,t,o,i,n){var r=A(n,t,e),p=H(o.placement,r,t,e,o.modifiers.flip.boundariesElement,o.modifiers.flip.padding);return t.setAttribute('x-placement',p),$(t,{position:'absolute'}),o}function ie(e,t){var o=Math.floor,i=t.x,n=t.y,r=e.offsets.popper,p=U(e.instance.modifiers,function(e){return'applyStyle'===e.name}).gpuAcceleration;void 0!==p&&console.warn('WARNING: `gpuAcceleration` option moved to `computeStyle` modifier and will not be supported in future versions of Popper.js!');var s,d,a=void 0===p?t.gpuAcceleration:p,l=m(e.instance.popper),f=N(l),h={position:r.position},c={left:o(r.left),top:o(r.top),bottom:o(r.bottom),right:o(r.right)},g='bottom'===i?'top':'bottom',u='right'===n?'left':'right',b=q('transform');if(d='bottom'==g?-f.height+c.bottom:c.top,s='right'==u?-f.width+c.right:c.left,a&&b)h[b]='translate3d('+s+'px, '+d+'px, 0)',h[g]=0,h[u]=0,h.willChange='transform';else{var w='bottom'==g?-1:1,y='right'==u?-1:1;h[g]=d*w,h[u]=s*y,h.willChange=g+', '+u}var E={"x-placement":e.placement};return e.attributes=T({},E,e.attributes),e.styles=T({},h,e.styles),e.arrowStyles=T({},e.offsets.arrow,e.arrowStyles),e}function ne(e,t,o){var i=U(e,function(e){var o=e.name;return o===t}),n=!!i&&e.some(function(e){return e.name===o&&e.enabled&&e.order<i.order});if(!n){var r='`'+t+'`';console.warn('`'+o+'`'+' modifier is required by '+r+' modifier in order to work, be sure to include it before '+r+'!')}return n}function re(e,t){var o;if(!ne(e.instance.modifiers,'arrow','keepTogether'))return e;var i=t.element;if('string'==typeof i){if(i=e.instance.popper.querySelector(i),!i)return e;}else if(!e.instance.popper.contains(i))return console.warn('WARNING: `arrow.element` must be child of its popper element!'),e;var n=e.placement.split('-')[0],r=e.offsets,p=r.popper,s=r.reference,d=-1!==['left','right'].indexOf(n),l=d?'height':'width',f=d?'Top':'Left',m=f.toLowerCase(),h=d?'left':'top',c=d?'bottom':'right',g=I(i)[l];s[c]-g<p[m]&&(e.offsets.popper[m]-=p[m]-(s[c]-g)),s[m]+g>p[c]&&(e.offsets.popper[m]+=s[m]+g-p[c]),e.offsets.popper=D(e.offsets.popper);var u=s[m]+s[l]/2-g/2,b=a(e.instance.popper),w=parseFloat(b['margin'+f],10),y=parseFloat(b['border'+f+'Width'],10),E=u-e.offsets.popper[m]-w-y;return E=Math.max(Math.min(p[l]-g,E),0),e.arrowElement=i,e.offsets.arrow=(o={},S(o,m,Math.round(E)),S(o,h,''),o),e}function pe(e){if('end'===e)return'start';return'start'===e?'end':e}var se=['auto-start','auto','auto-end','top-start','top','top-end','right-start','right','right-end','bottom-end','bottom','bottom-start','left-end','left','left-start'],de=se.slice(3);function ae(e){var t=1<arguments.length&&arguments[1]!==void 0&&arguments[1],o=de.indexOf(e),i=de.slice(o+1).concat(de.slice(0,o));return t?i.reverse():i}var le={FLIP:'flip',CLOCKWISE:'clockwise',COUNTERCLOCKWISE:'counterclockwise'};function fe(e,t){if(j(e.instance.modifiers,'inner'))return e;if(e.flipped&&e.placement===e.originalPlacement)return e;var o=P(e.instance.popper,e.instance.reference,t.padding,t.boundariesElement),i=e.placement.split('-')[0],n=M(i),r=e.placement.split('-')[1]||'',p=[];switch(t.behavior){case le.FLIP:p=[i,n];break;case le.CLOCKWISE:p=ae(i);break;case le.COUNTERCLOCKWISE:p=ae(i,!0);break;default:p=t.behavior;}return p.forEach(function(s,d){if(i!==s||p.length===d+1)return e;i=e.placement.split('-')[0],n=M(i);var a=e.offsets.popper,l=e.offsets.reference,f=Math.floor,m='left'===i&&f(a.right)>f(l.left)||'right'===i&&f(a.left)<f(l.right)||'top'===i&&f(a.bottom)>f(l.top)||'bottom'===i&&f(a.top)<f(l.bottom),h=f(a.left)<f(o.left),c=f(a.right)>f(o.right),g=f(a.top)<f(o.top),u=f(a.bottom)>f(o.bottom),b='left'===i&&h||'right'===i&&c||'top'===i&&g||'bottom'===i&&u,w=-1!==['top','bottom'].indexOf(i),y=!!t.flipVariations&&(w&&'start'===r&&h||w&&'end'===r&&c||!w&&'start'===r&&g||!w&&'end'===r&&u);(m||b||y)&&(e.flipped=!0,(m||b)&&(i=p[d+1]),y&&(r=pe(r)),e.placement=i+(r?'-'+r:''),e.offsets.popper=T({},e.offsets.popper,R(e.instance.popper,e.offsets.reference,e.placement)),e=F(e.instance.modifiers,e,'flip'))}),e}function me(e){var t=e.offsets,o=t.popper,i=t.reference,n=e.placement.split('-')[0],r=Math.floor,p=-1!==['top','bottom'].indexOf(n),s=p?'right':'bottom',d=p?'left':'top',a=p?'width':'height';return o[s]<r(i[d])&&(e.offsets.popper[d]=r(i[d])-o[a]),o[d]>r(i[s])&&(e.offsets.popper[d]=r(i[s])),e}function he(e,t,o,i){var n=Math.max,r=e.match(/((?:\-|\+)?\d*\.?\d*)(.*)/),p=+r[1],s=r[2];if(!p)return e;if(0===s.indexOf('%')){var d;switch(s){case'%p':d=o;break;case'%':case'%r':default:d=i;}var a=D(d);return a[t]/100*p}if('vh'===s||'vw'===s){var l;return l='vh'===s?n(document.documentElement.clientHeight,window.innerHeight||0):n(document.documentElement.clientWidth,window.innerWidth||0),l/100*p}return p}function ce(e,t,o,i){var n=[0,0],r=-1!==['right','left'].indexOf(i),p=e.split(/(\+|\-)/).map(function(e){return e.trim()}),s=p.indexOf(U(p,function(e){return-1!==e.search(/,|\s/)}));p[s]&&-1===p[s].indexOf(',')&&console.warn('Offsets separated by white space(s) are deprecated, use a comma (,) instead.');var d=/\s*,\s*|\s+/,a=-1===s?[p]:[p.slice(0,s).concat([p[s].split(d)[0]]),[p[s].split(d)[1]].concat(p.slice(s+1))];return a=a.map(function(e,i){var n=(1===i?!r:r)?'height':'width',p=!1;return e.reduce(function(e,t){return''===e[e.length-1]&&-1!==['+','-'].indexOf(t)?(e[e.length-1]=t,p=!0,e):p?(e[e.length-1]+=t,p=!1,e):e.concat(t)},[]).map(function(e){return he(e,n,t,o)})}),a.forEach(function(e,t){e.forEach(function(o,i){Z(o)&&(n[t]+=o*('-'===e[i-1]?-1:1))})}),n}function ge(e,t){var o,i=t.offset,n=e.placement,r=e.offsets,p=r.popper,s=r.reference,d=n.split('-')[0];return o=Z(+i)?[+i,0]:ce(i,p,s,d),'left'===d?(p.top+=o[0],p.left-=o[1]):'right'===d?(p.top+=o[0],p.left+=o[1]):'top'===d?(p.left+=o[0],p.top-=o[1]):'bottom'===d&&(p.left+=o[0],p.top+=o[1]),e.popper=p,e}function ue(e,t){var o=t.boundariesElement||m(e.instance.popper);e.instance.reference===o&&(o=m(o));var i=P(e.instance.popper,e.instance.reference,t.padding,o);t.boundaries=i;var n=t.priority,r=e.offsets.popper,p={primary:function(e){var o=r[e];return r[e]<i[e]&&!t.escapeWithReference&&(o=Math.max(r[e],i[e])),S({},e,o)},secondary:function(e){var o='right'===e?'left':'top',n=r[o];return r[e]>i[e]&&!t.escapeWithReference&&(n=Math.min(r[o],i[e]-('right'===e?r.width:r.height))),S({},o,n)}};return n.forEach(function(e){var t=-1===['left','top'].indexOf(e)?'secondary':'primary';r=T({},r,p[t](e))}),e.offsets.popper=r,e}function be(e){var t=e.placement,o=t.split('-')[0],i=t.split('-')[1];if(i){var n=e.offsets,r=n.reference,p=n.popper,s=-1!==['bottom','top'].indexOf(o),d=s?'left':'top',a=s?'width':'height',l={start:S({},d,r[d]),end:S({},d,r[d]+r[a]-p[a])};e.offsets.popper=T({},p,l[i])}return e}function we(e){if(!ne(e.instance.modifiers,'hide','preventOverflow'))return e;var t=e.offsets.reference,o=U(e.instance.modifiers,function(e){return'preventOverflow'===e.name}).boundaries;if(t.bottom<o.top||t.left>o.right||t.top>o.bottom||t.right<o.left){if(!0===e.hide)return e;e.hide=!0,e.attributes['x-out-of-boundaries']=''}else{if(!1===e.hide)return e;e.hide=!1,e.attributes['x-out-of-boundaries']=!1}return e}function ye(e){var t=e.placement,o=t.split('-')[0],i=e.offsets,n=i.popper,r=i.reference,p=-1!==['left','right'].indexOf(o),s=-1===['top','left'].indexOf(o);return n[p?'left':'top']=r[o]-(s?n[p?'width':'height']:0),e.placement=M(t),e.offsets.popper=D(n),e}var Ee={shift:{order:100,enabled:!0,fn:be},offset:{order:200,enabled:!0,fn:ge,offset:0},preventOverflow:{order:300,enabled:!0,fn:ue,priority:['left','right','top','bottom'],padding:5,boundariesElement:'scrollParent'},keepTogether:{order:400,enabled:!0,fn:me},arrow:{order:500,enabled:!0,fn:re,element:'[x-arrow]'},flip:{order:600,enabled:!0,fn:fe,behavior:'flip',padding:5,boundariesElement:'viewport'},inner:{order:700,enabled:!1,fn:ye},hide:{order:800,enabled:!0,fn:we},computeStyle:{order:850,enabled:!0,fn:ie,gpuAcceleration:!0,x:'bottom',y:'right'},applyStyle:{order:900,enabled:!0,fn:te,onLoad:oe,gpuAcceleration:void 0}},ve={placement:'bottom',eventsEnabled:!0,removeOnDestroy:!1,onCreate:function(){},onUpdate:function(){},modifiers:Ee},Oe=function(){function e(t,o){var i=this,n=2<arguments.length&&void 0!==arguments[2]?arguments[2]:{};x(this,e),this.scheduleUpdate=function(){return requestAnimationFrame(i.update)},this.update=s(this.update.bind(this)),this.options=T({},e.Defaults,n),this.state={isDestroyed:!1,isCreated:!1,scrollParents:[]},this.reference=t&&t.jquery?t[0]:t,this.popper=o&&o.jquery?o[0]:o,this.options.modifiers={},Object.keys(T({},e.Defaults.modifiers,n.modifiers)).forEach(function(t){i.options.modifiers[t]=T({},e.Defaults.modifiers[t]||{},n.modifiers?n.modifiers[t]:{})}),this.modifiers=Object.keys(this.options.modifiers).map(function(e){return T({name:e},i.options.modifiers[e])}).sort(function(e,t){return e.order-t.order}),this.modifiers.forEach(function(e){e.enabled&&d(e.onLoad)&&e.onLoad(i.reference,i.popper,i.options,e,i.state)}),this.update();var r=this.options.eventsEnabled;r&&this.enableEventListeners(),this.state.eventsEnabled=r}return L(e,[{key:'update',value:function(){return K.call(this)}},{key:'destroy',value:function(){return V.call(this)}},{key:'enableEventListeners',value:function(){return X.call(this)}},{key:'disableEventListeners',value:function(){return Q.call(this)}}]),e}();Oe.Utils=('undefined'==typeof window?global:window).PopperUtils,Oe.placements=se,Oe.Defaults=ve;export default Oe;
//# sourceMappingURL=popper.min.js.map