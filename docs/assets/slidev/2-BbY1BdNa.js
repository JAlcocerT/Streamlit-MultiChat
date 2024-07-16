import{d as $,r as T,A as f,o as i,c as y,k as _,f as g,b as p,y as k,F as w,ad as N,i as m,l as C,g as L,h as M,e as a,ay as D,aa as A,q as I,s as B,a6 as u}from"../modules/vue-CF22wb2R.js";import{a as H,ac as S}from"../index-KiKyF8R1.js";import{_ as V}from"./title-renderer.md_vue_type_script_setup_true_lang-BfqoKowG.js";import{u as P,f as z}from"./context-DDKcMwaC.js";import"../modules/shiki-Dk8qO-MX.js";const E=["href","innerHTML"],F=["href"],O=$({__name:"Link",props:{to:{},title:{}},setup(d){const{isPrintMode:l}=H();return(e,o)=>{const n=T("RouterLink");return!f(l)&&e.title?(i(),y(n,{key:0,to:String(e.to),onClick:o[0]||(o[0]=c=>c.target.blur()),innerHTML:e.title},null,8,["to","innerHTML"])):!f(l)&&!e.title?(i(),y(n,{key:1,to:String(e.to),onClick:o[1]||(o[1]=c=>c.target.blur())},{default:_(()=>[g(e.$slots,"default")]),_:3},8,["to"])):f(l)&&e.title?(i(),p("a",{key:2,href:`#${e.to}`,innerHTML:e.title},null,8,E)):(i(),p("a",{key:3,href:`#${e.to}`},[g(e.$slots,"default")],8,F))}}}),R=["start"],q=$({__name:"TocList",props:{level:{default:1},start:{},listStyle:{},list:{},listClass:{}},setup(d){const l=d,e=k(()=>[...S(l.listClass||[]),"slidev-toc-list",`slidev-toc-list-level-${l.level}`]),o=k(()=>[...S(l.listStyle||[])]);return(n,c)=>{const h=O,s=T("TocList",!0);return n.list&&n.list.length>0?(i(),p("ol",{key:0,class:m(e.value),start:n.level===1?n.start:void 0,style:M(o.value.length>=n.level?`list-style:${o.value[n.level-1]}`:void 0)},[(i(!0),p(w,null,N(n.list,t=>(i(),p("li",{key:t.path,class:m(["slidev-toc-item",[{"slidev-toc-item-active":t.active},{"slidev-toc-item-parent-active":t.activeParent}]])},[C(h,{to:t.path},{default:_(()=>[C(f(V),{no:t.no},null,8,["no"])]),_:2},1032,["to"]),t.children.length>0?(i(),y(s,{key:0,level:n.level+1,"list-style":n.listStyle,list:t.children,"list-class":n.listClass},null,8,["level","list-style","list","list-class"])):L("",!0)],2))),128))],14,R)):L("",!0)}}}),U=$({__name:"Toc",props:{columns:{default:1},listClass:{default:""},start:{default:1},listStyle:{default:""},maxDepth:{default:Number.POSITIVE_INFINITY},minDepth:{default:1},mode:{default:"all"}},setup(d){const l=d,{$slidev:e}=P();function o(s,t=1){if(t>Number(l.maxDepth))return[];if(t<Number(l.minDepth)){const r=s.find(v=>v.active||v.activeParent);return r?o(r.children,t+1):[]}return s.map(r=>({...r,children:o(r.children,t+1)}))}function n(s){return s.filter(t=>t.active||t.activeParent||t.hasActiveParent).map(t=>({...t,children:n(t.children)}))}function c(s){const t=s.some(r=>r.active||r.activeParent||r.hasActiveParent);return s.filter(()=>t).map(r=>({...r,children:c(r.children)}))}const h=k(()=>{const s=e==null?void 0:e.nav.tocTree;if(!s)return[];let t=o(s);return l.mode==="onlyCurrentTree"?t=n(t):l.mode==="onlySiblings"&&(t=c(t)),t});return(s,t)=>{const r=q;return i(),p("div",{class:"slidev-toc",style:M(`column-count:${s.columns}`)},[C(r,{level:1,start:s.start,"list-style":s.listStyle,list:h.value,"list-class":s.listClass},null,8,["start","list-style","list","list-class"])],4)}}}),W=$({__name:"two-cols",props:{class:{type:String},layoutClass:{type:String}},setup(d){const l=d;return(e,o)=>(i(),p("div",{class:m(["slidev-layout two-columns w-full h-full grid grid-cols-2",l.layoutClass])},[a("div",{class:m(["col-left",l.class])},[g(e.$slots,"default")],2),a("div",{class:m(["col-right",l.class])},[g(e.$slots,"right")],2)],2))}}),Y=a("h1",null,"Why Streamlit for a MultiChat App?",-1),j=a("p",null,"Streamlit can help to create a unified MultiChat app with Language Learning Models (LLMs)",-1),G=a("ul",null,[a("li",null,[u("🔄 "),a("strong",null,"Unified Experience"),u(" - Select different LLM providers from one place, without switching between platforms.")]),a("li",null,[u("👥 "),a("strong",null,"Multi-User Support"),u(" - Handle multiple users and conversations at once.")]),a("li",null,[u("🛠 "),a("strong",null,"Customizable"),u(" - Easily adapt the app to different learning methods and requirements.")]),a("li",null,[u("🌐 "),a("strong",null,"Web-Based"),u(" - Access your MultiChat app from anywhere, on any device.")])],-1),tt={__name:"2",setup(d){const{$slidev:l,$nav:e,$clicksContext:o,$clicks:n,$page:c,$renderContext:h,$frontmatter:s}=P();return(t,r)=>{const v=U,b=D("click");return i(),y(W,I(B(f(z)(f(s),1))),{right:_(J=>[A(C(v,{minDepth:"1",maxDepth:"2"},null,512),[[b]])]),default:_(()=>[Y,j,G]),_:1},16)}}};export{tt as default};
