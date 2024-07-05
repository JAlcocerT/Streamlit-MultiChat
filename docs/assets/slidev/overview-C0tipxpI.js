import{d as te,e as ne,_ as oe,f as le}from"../modules/unplugin-icons-Df0yGMHM.js";import{d as G,a7 as ie,a8 as ae,t as N,a9 as se,D as L,E as ce,a0 as re,n as J,H as m,o as a,c as $,i as S,h as R,aa as ue,ab as de,b as _,j as me,N as pe,y as W,S as fe,ac as ve,e as i,F as O,ad as P,k as V,g as M,x,l as y}from"../modules/vue-BxSvaxXU.js";import{u as he,a as ge,c as ke,C as U,g as j}from"../index-uJQwTELQ.js";import{b as _e,i as be,f as q,g as xe,p as ye}from"../monaco/bundled-types-BzndWMAD.js";import{u as we,S as Ce,_ as $e,a as Se}from"./DrawingPreview.vue_vue_type_script_setup_true_lang-C_WS0ndN.js";import{_ as z}from"./IconButton.vue_vue_type_script_setup_true_lang-BQDHB_ki.js";import{_ as De,C as Ee}from"./ClicksSlider-CGxFTsIp.js";import"../modules/shiki-t0KF6d4W.js";import"../modules/file-saver-igGfcqei.js";const He=["placeholder"],Me=G({__name:"NoteEditable",props:{no:{type:Number,required:!0},class:{default:""},editing:{default:!1},style:{default:()=>({})},placeholder:{default:"No notes for this slide"},clicksContext:{type:Object},highlight:{default:!0},autoHeight:{default:!1}},emits:["update:editing","markerDblclick","markerClick"],setup(w,{emit:A}){const o=w,b=A,c=ie(o,"editing",b,{passive:!0}),{info:f,update:D}=we(ae(o,"no")),v=N("");let E;const{ignoreUpdates:g}=se(v,u=>{if(!c.value)return;const d=o.no;clearTimeout(E),E=setTimeout(()=>{D({note:u},d)},500)});L(()=>{var u;return(u=f.value)==null?void 0:u.note},(u="")=>{c.value||(clearTimeout(E),g(()=>{v.value=u}))},{immediate:!0,flush:"sync"});const r=N(),k=N();ce(()=>{var u;c.value&&((u=r.value)==null||u.focus())}),re(r,()=>{c.value=!1});function T(){!o.autoHeight||!r.value||!c.value||r.value.scrollHeight>r.value.clientHeight&&(r.value.style.height=`${r.value.scrollHeight}px`)}return L([v,c],()=>{J(()=>{T()})},{flush:"post",immediate:!0}),(u,d)=>{var B;return m(c)?ue((a(),_("textarea",{key:1,ref_key:"inputEl",ref:r,"onUpdate:modelValue":d[2]||(d[2]=h=>v.value=h),class:S(["prose resize-none overflow-auto outline-none bg-transparent block border-primary border-2",o.class]),style:R([{"line-height":"1.75"},[o.style,k.value!=null?{height:`${k.value}px`}:{}]]),placeholder:w.placeholder,onKeydown:d[3]||(d[3]=me(h=>c.value=!1,["esc"]))},null,46,He)),[[de,v.value]]):(a(),$(De,{key:0,class:S(["border-transparent border-2",[o.class,v.value?"":"opacity-25 italic select-none"]]),style:R(o.style),note:v.value||w.placeholder,"note-html":(B=m(f))==null?void 0:B.noteHTML,"clicks-context":w.clicksContext,"auto-scroll":!w.autoHeight,highlight:o.highlight,onMarkerClick:d[0]||(d[0]=(h,C)=>b("markerClick",h,C)),onMarkerDblclick:d[1]||(d[1]=(h,C)=>b("markerDblclick",h,C))},null,8,["class","style","note","note-html","clicks-context","auto-scroll","highlight"]))}}}),Ne={class:"h-screen w-screen of-hidden flex"},Te={class:"grid grid-rows-[auto_max-content] border-r border-main select-none max-h-full h-full"},Be={class:"relative"},Ie={class:"absolute left-0 top-0 bottom-0 w-200 flex flex-col flex-auto items-end group p2 gap-1 max-h-full of-x-visible of-y-auto",style:{direction:"rtl"}},Ve=["onClick"],We={p2:"",border:"t main"},ze={class:"select-none w-13 text-right my4 flex flex-col gap-1 items-end"},Re={class:"text-3xl op20 mb2"},Ae={class:"flex flex-col gap-2 my5"},Fe=["onDblclick"],Ke={class:"py3 mt-0.5 mr--8 ml--4 op0 transition group-hover:op100"},Le={key:0,class:"select-none absolute bottom-0 right-0 bg-main rounded-tl p2 op35 text-xs"},Oe={class:"absolute top-0 right-0 px3 py1.5 border-b border-l rounded-lb bg-main border-main select-none"},Pe={class:"text-xs op50"},X=450,tt=G({__name:"overview",setup(w){he({title:`Overview - ${_e}`});const{openInEditor:A,slides:o}=ge(),b=pe(new Map),c=N([]),f=N(null),D=W(()=>o.value.map(t=>{var e,l;return d(((l=(e=t.meta)==null?void 0:e.slide)==null?void 0:l.note)||"")})),v=W(()=>D.value.reduce((t,e)=>t+e,0)),E=W(()=>o.value.map(t=>T(t)).reduce((t,e)=>t+e,0)),g=fe(),r=new WeakMap;function k(t){return r.has(t)||r.set(t,ke(t,U)),r.get(t)}function T(t){var e,l;return((e=t.meta)==null?void 0:e.clicks)||((l=k(t))==null?void 0:l.total)}function u(t){g.value===t?g.value=void 0:g.value=t}function d(t){var e;return((e=t.match(/[\w`'\-]+/g))==null?void 0:e.length)||0}function B(t){const e=t.getBoundingClientRect(),l=20;return e.top>=0-l&&e.left>=0-l&&e.bottom<=(window.innerHeight||document.documentElement.clientHeight)+l&&e.right<=(window.innerWidth||document.documentElement.clientWidth)+l}function h(){const t=[];Array.from(b.entries()).forEach(([e,l])=>{B(l)&&t.push(e)}),c.value=t}function C(t){const e=document.createElement("a");e.target="_blank",e.href=ye+t.slice(1),e.click()}function Q(t){const e=b.get(t);e&&e.scrollIntoView({behavior:"smooth",block:"start"})}function Y(t,e,l){const H=k(l);H.current===e?H.current=U:H.current=e,t.preventDefault()}return ve(()=>{J(()=>{h()})}),(t,e)=>{const l=te,H=ne,Z=oe,ee=le;return a(),_("div",Ne,[i("nav",Te,[i("div",Be,[i("div",Ie,[(a(!0),_(O,null,P(m(o),(n,p)=>{var s,I,F,K;return a(),_("div",{key:n.no,class:"relative",style:{direction:"ltr"}},[i("button",{class:S(["relative transition duration-300 w-8 h-8 rounded hover:bg-active hover:op100",c.value.includes(p)?"op100 text-primary bg-gray:5":"op20"]),onClick:Ue=>Q(p)},[i("div",null,x(p+1),1)],10,Ve),(I=(s=n.meta)==null?void 0:s.slide)!=null&&I.title?(a(),_("div",{key:0,class:S(["pointer-events-none select-none absolute left-110% backdrop-blur-8 top-50% translate-y--50% ws-nowrap z-10 px2 shadow-xl rounded border border-main transition duration-400 op0 group-hover:op100",c.value.includes(p)?"text-primary":"text-main important-text-op-50"])},x((K=(F=n.meta)==null?void 0:F.slide)==null?void 0:K.title),3)):M("v-if",!0)])}),128))])]),i("div",We,[m(be)?M("v-if",!0):(a(),$(z,{key:0,title:m(q)?"Switch to light mode theme":"Switch to dark mode theme",onClick:e[0]||(e[0]=n=>m(xe)())},{default:V(()=>[m(q)?(a(),$(l,{key:0})):(a(),$(H,{key:1}))]),_:1},8,["title"]))])]),i("main",{class:"flex-1 h-full of-auto",style:R(`grid-template-columns: repeat(auto-fit,minmax(${X}px,1fr))`),onScroll:h},[(a(!0),_(O,null,P(m(o),(n,p)=>(a(),_("div",{key:n.no,ref_for:!0,ref:s=>b.set(p,s),class:S(["relative border-t border-main of-hidden flex gap-4 min-h-50 group",p===0?"pt5":""])},[i("div",ze,[i("div",Re,x(p+1),1),y(z,{class:"mr--3 op0 group-hover:op80",title:"Play in new tab",onClick:s=>C(m(j)(n,!1))},{default:V(()=>[y(Z)]),_:2},1032,["onClick"]),M("v-if",!0)]),i("div",Ae,[i("div",{class:"border rounded border-main overflow-hidden bg-main select-none h-max",onDblclick:s=>C(m(j)(n,!1))},[(a(),$(Se,{key:n.no,width:X,class:"pointer-events-none important:[&_*]:select-none"},{default:V(()=>[y(Ce,{"clicks-context":k(n),route:n,"render-context":"overview"},null,8,["clicks-context","route"]),y($e,{page:n.no},null,8,["page"])]),_:2},1024))],40,Fe),T(n)?(a(),$(Ee,{key:0,active:g.value===n,"clicks-context":k(n),class:"w-full mt-2",onDblclick:s=>u(n),onClick:s=>g.value=n},null,8,["active","clicks-context","onDblclick","onClick"])):M("v-if",!0)]),i("div",Ke,[y(z,{title:"Edit Note",class:S(["rounded-full w-9 h-9 text-sm",f.value===n.no?"important:op0":""]),onClick:s=>f.value=n.no},{default:V(()=>[y(ee)]),_:2},1032,["class","onClick"])]),y(Me,{no:n.no,class:"max-w-250 w-250 text-lg rounded p3","auto-height":!0,highlight:g.value===n,editing:f.value===n.no,"clicks-context":k(n),onDblclick:s=>f.value!==n.no?f.value=n.no:null,"onUpdate:editing":e[1]||(e[1]=s=>f.value=null),onMarkerClick:(s,I)=>Y(s,I,n)},null,8,["no","highlight","editing","clicks-context","onDblclick","onMarkerClick"]),D.value[p]>0?(a(),_("div",Le,x(D.value[p])+" words ",1)):M("v-if",!0)],2))),128))],36),i("div",Oe,[i("div",Pe,x(m(o).length)+" slides · "+x(E.value+m(o).length-1)+" clicks · "+x(v.value)+" words ",1)])])}}});export{tt as default};
