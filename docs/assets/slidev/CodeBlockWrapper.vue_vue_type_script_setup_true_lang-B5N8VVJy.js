import{D as L,E as w}from"../modules/unplugin-icons-kZaMBlYE.js";import{d as A,t as I,aB as B,E as y,ac as N,y as v,aF as q,o as c,b as _,f as M,H as u,c as C,g as V,i as $,h as D}from"../modules/vue-CSlgF7c5.js";import{c as k}from"../monaco/bundled-types-GpUe0cbt.js";import{$ as z,C as K,a2 as R,a0 as F}from"../index-Bkx_WD9F.js";import{u as U}from"./context-LhTc2K18.js";const W=["title"],Q=A({__name:"CodeBlockWrapper",props:{ranges:{type:Array,default:()=>[]},finally:{type:[String,Number],default:"last"},startLine:{type:Number,default:1},lines:{type:Boolean,default:k.lineNumbers},at:{type:[String,Number],default:"+1"},maxHeight:{type:String,default:void 0}},setup(S){const e=S,{$clicksContext:a}=U(),s=I(),d=z();B(()=>{a.unregister(d)}),y(()=>{var t;(t=s.value)==null||t.classList.toggle("slidev-code-line-numbers",e.lines)}),N(()=>{var r;if(!a||!((r=e.ranges)!=null&&r.length))return;const t=a.calculateSince(e.at,e.ranges.length-1);a.register(d,t);const o=v(()=>t?Math.max(0,a.current-t.start+1):K),n=v(()=>e.finally==="last"?e.ranges.at(-1):e.finally.toString());y(()=>{if(!s.value)return;let i=e.ranges[o.value]??n.value;const g=i==="hide";s.value.classList.toggle(R,g),g&&(i=e.ranges[o.value+1]??n.value);const h=s.value.querySelector(".shiki"),m=Array.from(h.querySelectorAll("code > .line")),H=m.length;if(F(i,H,e.startLine,l=>[m[l]]),e.maxHeight){const l=Array.from(h.querySelectorAll(".line.highlighted"));l.reduce((f,E)=>E.offsetHeight+f,0)>s.value.offsetHeight?l[0].scrollIntoView({behavior:"smooth",block:"start"}):l.length>0&&l[Math.round((l.length-1)/2)].scrollIntoView({behavior:"smooth",block:"center"})}})});const{copied:p,copy:b}=q();function x(){var o,n;const t=(n=(o=s.value)==null?void 0:o.querySelector(".slidev-code"))==null?void 0:n.textContent;t&&b(t)}return(t,o)=>{const n=L,r=w;return c(),_("div",{ref_key:"el",ref:s,class:$(["slidev-code-wrapper relative group",{"slidev-code-line-numbers":e.lines}]),style:D({"max-height":e.maxHeight,"overflow-y":e.maxHeight?"scroll":void 0,"--start":e.startLine})},[M(t.$slots,"default"),u(k).codeCopy?(c(),_("button",{key:0,class:"slidev-code-copy absolute top-0 right-0 transition opacity-0 group-hover:opacity-20 hover:!opacity-100",title:u(p)?"Copied":"Copy",onClick:o[0]||(o[0]=i=>x())},[u(p)?(c(),C(n,{key:0,class:"p-2 w-8 h-8"})):(c(),C(r,{key:1,class:"p-2 w-8 h-8"}))],8,W)):V("",!0)],6)}}});export{Q as _};