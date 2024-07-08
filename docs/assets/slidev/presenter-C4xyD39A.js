import{g as G,h as j,k as q,l as A}from"../modules/unplugin-icons-kZaMBlYE.js";import{d as M,o,c,i as P,H as e,t as N,y as g,D as z,S as J,ac as K,N as O,ae as Q,a1 as U,b as y,e as s,l as t,k as h,g as F,h as I,x as X,F as Y,p as Z,a as ee}from"../modules/vue-CSlgF7c5.js";import{a as te,u as se,d as oe,c as ne,s as ae,e as re,p as ie,h as le,i as ce,j as ue,k as pe,_ as de}from"../index-Bkx_WD9F.js";import{r as me,u as _e,a as fe,S as xe,_ as ve,G as ke,b as he,c as be,o as ge}from"./useWakeLock-m_RPHfbC.js";import{b as ye}from"../monaco/bundled-types-GpUe0cbt.js";import{b as Ce,c as Se,a as B,S as we}from"./DrawingPreview.vue_vue_type_script_setup_true_lang-VCQl1c1D.js";import{_ as $e,C as Ne}from"./ClicksSlider-xAa07_4P.js";import{_ as ze}from"./DrawingControls.vue_vue_type_style_index_0_lang-CYgHMJV_.js";import{_ as D}from"./IconButton.vue_vue_type_script_setup_true_lang-C21a9sE8.js";import"../modules/shiki-WYk1xoOD.js";import"../modules/file-saver-igGfcqei.js";import"./title-renderer.md_vue_type_script_setup_true_lang-DmNH3-wm.js";import"./context-LhTc2K18.js";const Fe=M({__name:"NoteStatic",props:{no:{},class:{},clicksContext:{}},setup(i){const l=i,{info:r}=Ce(l.no);return(u,_)=>{var f,x;return o(),c($e,{class:P(l.class),note:(f=e(r))==null?void 0:f.note,"note-html":(x=e(r))==null?void 0:x.noteHTML,"clicks-context":u.clicksContext},null,8,["class","note","note-html","clicks-context"])}}}),C=i=>(Z("data-v-85e4371b"),i=i(),ee(),i),Ie={class:"bg-main h-full slidev-presenter"},Be=C(()=>s("div",{class:"absolute left-0 top-0 bg-main border-b border-r border-main px2 py1 op50 text-sm"}," Current ",-1)),De={class:"relative grid-section next flex flex-col p-2 lg:p-4"},Me=C(()=>s("div",{class:"absolute left-0 top-0 bg-main border-b border-r border-main px2 py1 op50 text-sm"}," Next ",-1)),Pe={key:0,class:"grid-section note of-auto"},Re={key:1,class:"grid-section note grid grid-rows-[1fr_min-content] overflow-hidden"},Te={class:"border-t border-main py-1 px-2 text-sm"},Ee={class:"grid-section bottom flex"},He=C(()=>s("div",{"flex-auto":""},null,-1)),Le={class:"text-2xl pl-2 pr-6 my-auto tabular-nums"},Ve={class:"progress-bar"},We=M({__name:"presenter",setup(i){const l=N();me(),_e(l),fe();const{clicksContext:r,currentSlideNo:u,currentSlideRoute:_,hasNext:f,nextRoute:x,slides:R,getPrimaryClicks:T,total:E}=te(),{isDrawing:H}=Se();se({title:`Presenter - ${ye}`}),N(!1);const{timer:L,resetTimer:S}=oe(),V=g(()=>R.value.map(k=>ne(k))),n=g(()=>r.value.current<r.value.total?[_.value,r.value.current+1]:f.value?[x.value,0]:null),v=g(()=>n.value&&V.value[n.value[0].no-1]);z(n,()=>{v.value&&n.value&&(v.value.current=n.value[1])},{immediate:!0});const w=J();return K(()=>{const k=l.value.querySelector("#slide-content"),p=O(Q()),b=U();z(()=>{if(!b.value||H.value||!re.value)return;const a=k.getBoundingClientRect(),d=(p.x-a.left)/a.width*100,m=(p.y-a.top)/a.height*100;if(!(d<0||d>100||m<0||m>100))return{x:d,y:m}},a=>{ae.cursor=a})}),(k,p)=>{var $;const b=G,a=j,d=q,m=A;return o(),y(Y,null,[s("div",Ie,[s("div",{class:P(["grid-container",`layout${e(ie)}`])},[s("div",{ref_key:"main",ref:l,class:"relative grid-section main flex flex-col"},[t(B,{key:"main",class:"p-2 lg:p-4 flex-auto","is-main":"",onContextmenu:e(ge)},{default:h(()=>[t(xe,{"render-context":"presenter"})]),_:1},8,["onContextmenu"]),(o(),c(Ne,{key:($=e(_))==null?void 0:$.no,"clicks-context":e(T)(e(_)),class:"w-full pb2 px4 flex-none"},null,8,["clicks-context"])),Be],512),s("div",De,[n.value&&v.value?(o(),c(B,{key:"next"},{default:h(()=>[(o(),c(we,{key:n.value[0].no,"clicks-context":v.value,route:n.value[0],"render-context":"previewNext"},null,8,["clicks-context","route"]))]),_:1})):F("",!0),Me]),w.value&&e(le)?(o(),y("div",Pe,[t(e(w))])):(o(),y("div",Re,[(o(),c(Fe,{key:`static-${e(u)}`,no:e(u),class:"w-full max-w-full h-full overflow-auto p-2 lg:p-4",style:I({fontSize:`${e(ce)}em`}),"clicks-context":e(r)},null,8,["no","style","clicks-context"])),s("div",Te,[t(D,{title:"Increase font size",onClick:e(ue)},{default:h(()=>[t(b)]),_:1},8,["onClick"]),t(D,{title:"Decrease font size",onClick:e(pe)},{default:h(()=>[t(a)]),_:1},8,["onClick"]),F("",!0)])])),s("div",Ee,[t(ve,{persist:!0}),He,s("div",{class:"timer-btn my-auto relative w-22px h-22px cursor-pointer text-lg",opacity:"50 hover:100",onClick:p[2]||(p[2]=(...W)=>e(S)&&e(S)(...W))},[t(d,{class:"absolute"}),t(m,{class:"absolute opacity-0"})]),s("div",Le,X(e(L)),1)]),(o(),c(ze,{key:2}))],2),s("div",Ve,[s("div",{class:"progress h-3px bg-primary transition-all",style:I({width:`${(e(u)-1)/(e(E)-1)*100+1}%`})},null,4)])]),t(ke),t(he),t(be)],64)}}}),tt=de(We,[["__scopeId","data-v-85e4371b"]]);export{tt as default};