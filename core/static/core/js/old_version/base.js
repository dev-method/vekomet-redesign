!function(n){"function"==typeof define&&define.amd?define(["jquery"],function(e){return n(e)}):"object"==typeof module&&"object"==typeof module.exports?exports=n(require("jquery")):n(jQuery)}(function(n){function t(e){var n=7.5625,t=2.75;return e<1/t?n*e*e:e<2/t?n*(e-=1.5/t)*e+.75:e<2.5/t?n*(e-=2.25/t)*e+.9375:n*(e-=2.625/t)*e+.984375}void 0!==n.easing&&(n.easing.jswing=n.easing.swing);var i=Math.pow,a=Math.sqrt,s=Math.sin,o=Math.cos,r=Math.PI,l=1.70158,c=1.525*l,u=2*r/3,p=2*r/4.5;n.extend(n.easing,{def:"easeOutQuad",swing:function(e){return n.easing[n.easing.def](e)},easeInQuad:function(e){return e*e},easeOutQuad:function(e){return 1-(1-e)*(1-e)},easeInOutQuad:function(e){return e<.5?2*e*e:1-i(-2*e+2,2)/2},easeInCubic:function(e){return e*e*e},easeOutCubic:function(e){return 1-i(1-e,3)},easeInOutCubic:function(e){return e<.5?4*e*e*e:1-i(-2*e+2,3)/2},easeInQuart:function(e){return e*e*e*e},easeOutQuart:function(e){return 1-i(1-e,4)},easeInOutQuart:function(e){return e<.5?8*e*e*e*e:1-i(-2*e+2,4)/2},easeInQuint:function(e){return e*e*e*e*e},easeOutQuint:function(e){return 1-i(1-e,5)},easeInOutQuint:function(e){return e<.5?16*e*e*e*e*e:1-i(-2*e+2,5)/2},easeInSine:function(e){return 1-o(e*r/2)},easeOutSine:function(e){return s(e*r/2)},easeInOutSine:function(e){return-(o(r*e)-1)/2},easeInExpo:function(e){return 0===e?0:i(2,10*e-10)},easeOutExpo:function(e){return 1===e?1:1-i(2,-10*e)},easeInOutExpo:function(e){return 0===e?0:1===e?1:e<.5?i(2,20*e-10)/2:(2-i(2,-20*e+10))/2},easeInCirc:function(e){return 1-a(1-i(e,2))},easeOutCirc:function(e){return a(1-i(e-1,2))},easeInOutCirc:function(e){return e<.5?(1-a(1-i(2*e,2)))/2:(a(1-i(-2*e+2,2))+1)/2},easeInElastic:function(e){return 0===e?0:1===e?1:-i(2,10*e-10)*s((10*e-10.75)*u)},easeOutElastic:function(e){return 0===e?0:1===e?1:i(2,-10*e)*s((10*e-.75)*u)+1},easeInOutElastic:function(e){return 0===e?0:1===e?1:e<.5?-i(2,20*e-10)*s((20*e-11.125)*p)/2:i(2,-20*e+10)*s((20*e-11.125)*p)/2+1},easeInBack:function(e){return(l+1)*e*e*e-l*e*e},easeOutBack:function(e){return 1+(l+1)*i(e-1,3)+l*i(e-1,2)},easeInOutBack:function(e){return e<.5?i(2*e,2)*(7.189819*e-c)/2:(i(2*e-2,2)*((c+1)*(2*e-2)+c)+2)/2},easeInBounce:function(e){return 1-t(1-e)},easeOutBounce:t,easeInOutBounce:function(e){return e<.5?(1-t(1-2*e))/2:(1+t(2*e-1))/2}})}),function(e){"function"==typeof define&&define.amd?define(["jquery"],e):"object"==typeof exports?module.exports=e(require("jquery")):e(jQuery)}(function(m){var i=/\+/g;function h(e){return g.raw?e:encodeURIComponent(e)}function v(e,n){var t=g.raw?e:function(e){0===e.indexOf('"')&&(e=e.slice(1,-1).replace(/\\"/g,'"').replace(/\\\\/g,"\\"));try{return e=decodeURIComponent(e.replace(i," ")),g.json?JSON.parse(e):e}catch(e){}}(e);return m.isFunction(n)?n(t):t}var g=m.cookie=function(e,n,t){if(1<arguments.length&&!m.isFunction(n)){if("number"==typeof(t=m.extend({},g.defaults,t)).expires){var i=t.expires,a=t.expires=new Date;a.setMilliseconds(a.getMilliseconds()+864e5*i)}return document.cookie=[h(e),"=",(s=n,h(g.json?JSON.stringify(s):String(s))),t.expires?"; expires="+t.expires.toUTCString():"",t.path?"; path="+t.path:"",t.domain?"; domain="+t.domain:"",t.secure?"; secure":""].join("")}for(var s,o,r=e?void 0:{},l=document.cookie?document.cookie.split("; "):[],c=0,u=l.length;c<u;c++){var p=l[c].split("="),d=(o=p.shift(),g.raw?o:decodeURIComponent(o)),f=p.join("=");if(e===d){r=v(f,n);break}e||void 0===(f=v(f))||(r[d]=f)}return r};g.defaults={},m.removeCookie=function(e,n){return m.cookie(e,"",m.extend({},n,{expires:-1})),!m.cookie(e)}}),function(p,s,e){function a(e,n){this.element=e,this.settings=p.extend({},t,n),this.settings.duplicate||n.hasOwnProperty("removeIds")||(this.settings.removeIds=!1),this._defaults=t,this._name=o,this.init()}var t={label:"MENU",duplicate:!0,duration:200,easingOpen:"swing",easingClose:"swing",closedSymbol:"&#9658;",openedSymbol:"&#9660;",prependTo:"body",appendTo:"",parentTag:"a",closeOnClick:!1,allowParentLinks:!1,nestedParentLinks:!0,showChildren:!1,removeIds:!0,removeClasses:!1,removeStyles:!1,brand:"",animations:"jquery",init:function(){},beforeOpen:function(){},beforeClose:function(){},afterOpen:function(){},afterClose:function(){}},o="slicknav",d="slicknav",c=40,u=13,f=27,m=37,h=39,v=32,g=38;a.prototype.init=function(){var e,n,r=this,t=p(this.element),l=this.settings;if(l.duplicate?r.mobileNav=t.clone():r.mobileNav=t,l.removeIds&&(r.mobileNav.removeAttr("id"),r.mobileNav.find("*").each(function(e,n){p(n).removeAttr("id")})),l.removeClasses&&(r.mobileNav.removeAttr("class"),r.mobileNav.find("*").each(function(e,n){p(n).removeAttr("class")})),l.removeStyles&&(r.mobileNav.removeAttr("style"),r.mobileNav.find("*").each(function(e,n){p(n).removeAttr("style")})),e=d+"_icon",""===l.label&&(e+=" "+d+"_no-text"),"a"==l.parentTag&&(l.parentTag='a href="#"'),r.mobileNav.attr("class",d+"_nav"),n=p('<div class="'+d+'_menu"></div>'),""!==l.brand){var i=p('<div class="'+d+'_brand">'+l.brand+"</div>");p(n).append(i)}r.btn=p(["<"+l.parentTag+' aria-haspopup="true" role="button" tabindex="0" class="'+d+"_btn "+d+'_collapsed">','<span class="'+d+'_menutxt">'+l.label+"</span>",'<span class="'+e+'">','<span class="'+d+'_icon-bar"></span>','<span class="'+d+'_icon-bar"></span>','<span class="'+d+'_icon-bar"></span>',"</span>","</"+l.parentTag+">"].join("")),p(n).append(r.btn),""!==l.appendTo?p(l.appendTo).append(n):p(l.prependTo).prepend(n),n.append(r.mobileNav);var a=r.mobileNav.find("li");p(a).each(function(){var e=p(this),n={};if(n.children=e.children("ul").attr("role","menu"),e.data("menu",n),0<n.children.length){var t=e.contents(),i=!1,a=[];p(t).each(function(){return!p(this).is("ul")&&(a.push(this),void(p(this).is("a")&&(i=!0)))});var s=p("<"+l.parentTag+' role="menuitem" aria-haspopup="true" tabindex="-1" class="'+d+'_item"/>');if(l.allowParentLinks&&!l.nestedParentLinks&&i)p(a).wrapAll('<span class="'+d+"_parent-link "+d+'_row"/>').parent();else p(a).wrapAll(s).parent().addClass(d+"_row");l.showChildren?e.addClass(d+"_open"):e.addClass(d+"_collapsed"),e.addClass(d+"_parent");var o=p('<span class="'+d+'_arrow">'+(l.showChildren?l.openedSymbol:l.closedSymbol)+"</span>");l.allowParentLinks&&!l.nestedParentLinks&&i&&(o=o.wrap(s).parent()),p(a).last().after(o)}else 0===e.children().length&&e.addClass(d+"_txtnode");e.children("a").attr("role","menuitem").click(function(e){l.closeOnClick&&!p(e.target).parent().closest("li").hasClass(d+"_parent")&&p(r.btn).click()}),l.closeOnClick&&l.allowParentLinks&&(e.children("a").children("a").click(function(e){p(r.btn).click()}),e.find("."+d+"_parent-link a:not(."+d+"_item)").click(function(e){p(r.btn).click()}))}),p(a).each(function(){var e=p(this).data("menu");l.showChildren||r._visibilityToggle(e.children,null,!1,null,!0)}),r._visibilityToggle(r.mobileNav,null,!1,"init",!0),r.mobileNav.attr("role","menu"),p(s).mousedown(function(){r._outlines(!1)}),p(s).keyup(function(){r._outlines(!0)}),p(r.btn).click(function(e){e.preventDefault(),r._menuToggle()}),r.mobileNav.on("click","."+d+"_item",function(e){e.preventDefault(),r._itemClick(p(this))}),p(r.btn).keydown(function(e){var n=e||event;switch(n.keyCode){case u:case v:case c:e.preventDefault(),n.keyCode===c&&p(r.btn).hasClass(d+"_open")||r._menuToggle(),p(r.btn).next().find('[role="menuitem"]').first().focus()}}),r.mobileNav.on("keydown","."+d+"_item",function(e){switch((e||event).keyCode){case u:e.preventDefault(),r._itemClick(p(e.target));break;case h:e.preventDefault(),p(e.target).parent().hasClass(d+"_collapsed")&&r._itemClick(p(e.target)),p(e.target).next().find('[role="menuitem"]').first().focus()}}),r.mobileNav.on("keydown",'[role="menuitem"]',function(e){switch((e||event).keyCode){case c:e.preventDefault();var n=(i=(t=p(e.target).parent().parent().children().children('[role="menuitem"]:visible')).index(e.target))+1;t.length<=n&&(n=0),t.eq(n).focus();break;case g:e.preventDefault();var t,i=(t=p(e.target).parent().parent().children().children('[role="menuitem"]:visible')).index(e.target);t.eq(i-1).focus();break;case m:if(e.preventDefault(),p(e.target).parent().parent().parent().hasClass(d+"_open")){var a=p(e.target).parent().parent().prev();a.focus(),r._itemClick(a)}else p(e.target).parent().parent().hasClass(d+"_nav")&&(r._menuToggle(),p(r.btn).focus());break;case f:e.preventDefault(),r._menuToggle(),p(r.btn).focus()}}),l.allowParentLinks&&l.nestedParentLinks&&p("."+d+"_item a").click(function(e){e.stopImmediatePropagation()})},a.prototype._menuToggle=function(e){var n=this.btn,t=this.mobileNav;n.hasClass(d+"_collapsed")?(n.removeClass(d+"_collapsed"),n.addClass(d+"_open")):(n.removeClass(d+"_open"),n.addClass(d+"_collapsed")),n.addClass(d+"_animating"),this._visibilityToggle(t,n.parent(),!0,n)},a.prototype._itemClick=function(e){var n=this.settings,t=e.data("menu");t||((t={}).arrow=e.children("."+d+"_arrow"),t.ul=e.next("ul"),t.parent=e.parent(),t.parent.hasClass(d+"_parent-link")&&(t.parent=e.parent().parent(),t.ul=e.parent().next("ul")),e.data("menu",t)),t.parent.hasClass(d+"_collapsed")?(t.arrow.html(n.openedSymbol),t.parent.removeClass(d+"_collapsed"),t.parent.addClass(d+"_open")):(t.arrow.html(n.closedSymbol),t.parent.addClass(d+"_collapsed"),t.parent.removeClass(d+"_open")),t.parent.addClass(d+"_animating"),this._visibilityToggle(t.ul,t.parent,!0,e)},a.prototype._visibilityToggle=function(t,e,n,i,a){function s(e,n){p(e).removeClass(d+"_animating"),p(n).removeClass(d+"_animating"),a||l.afterOpen(e)}function o(e,n){t.attr("aria-hidden","true"),c.attr("tabindex","-1"),r._setVisAttr(t,!0),t.hide(),p(e).removeClass(d+"_animating"),p(n).removeClass(d+"_animating"),a?"init"==e&&l.init():l.afterClose(e)}var r=this,l=r.settings,c=r._getActionItems(t),u=0;n&&(u=l.duration),t.hasClass(d+"_hidden")?(t.removeClass(d+"_hidden"),a||l.beforeOpen(i),"jquery"===l.animations?t.stop(!0,!0).slideDown(u,l.easingOpen,function(){s(i,e)}):"velocity"===l.animations&&t.velocity("finish").velocity("slideDown",{duration:u,easing:l.easingOpen,complete:function(){s(i,e)}}),t.attr("aria-hidden","false"),c.attr("tabindex","0"),r._setVisAttr(t,!1)):(t.addClass(d+"_hidden"),a||l.beforeClose(i),"jquery"===l.animations?t.stop(!0,!0).slideUp(u,this.settings.easingClose,function(){o(i,e)}):"velocity"===l.animations&&t.velocity("finish").velocity("slideUp",{duration:u,easing:l.easingClose,complete:function(){o(i,e)}}))},a.prototype._setVisAttr=function(e,n){var t=this,i=e.children("li").children("ul").not("."+d+"_hidden");n?i.each(function(){var e=p(this);e.attr("aria-hidden","true"),t._getActionItems(e).attr("tabindex","-1"),t._setVisAttr(e,n)}):i.each(function(){var e=p(this);e.attr("aria-hidden","false"),t._getActionItems(e).attr("tabindex","0"),t._setVisAttr(e,n)})},a.prototype._getActionItems=function(e){var n=e.data("menu");if(!n){n={};var t=e.children("li"),i=t.find("a");n.links=i.add(t.find("."+d+"_item")),e.data("menu",n)}return n.links},a.prototype._outlines=function(e){e?p("."+d+"_item, ."+d+"_btn").css("outline",""):p("."+d+"_item, ."+d+"_btn").css("outline","none")},a.prototype.toggle=function(){this._menuToggle()},a.prototype.open=function(){this.btn.hasClass(d+"_collapsed")&&this._menuToggle()},a.prototype.close=function(){this.btn.hasClass(d+"_open")&&this._menuToggle()},p.fn[o]=function(n){var t,i=arguments;return void 0===n||"object"==typeof n?this.each(function(){p.data(this,"plugin_"+o)||p.data(this,"plugin_"+o,new a(this,n))}):"string"==typeof n&&"_"!==n[0]&&"init"!==n?(this.each(function(){var e=p.data(this,"plugin_"+o);e instanceof a&&"function"==typeof e[n]&&(t=e[n].apply(e,Array.prototype.slice.call(i,1)))}),void 0!==t?t:this):void 0}}(jQuery,document,window),function(p){p.fn.UItoTop=function(e){var n={text:"",min:200,scrollSpeed:800,containerID:"toTop",containerHoverID:"toTopHover",easingType:"linear",min_width:parseInt(p("body").css("min-width"),10),main_width:parseInt(p("body").css("min-width"),10)/2},t=p.extend(n,e),i="#"+t.containerID,a="#"+t.containerHoverID;p("body").append('<a href="#" id="'+t.containerID+'">'+t.text+"</a>");var s=parseInt(p(i).css("width"))+90,o=parseInt(p(i).css("width"))+20,r=n.min_width+s,l=-(n.main_width+o),c=-(n.main_width-20);function u(){p(window).width()<=r&&p(window).width()>=n.min_width?p(i).stop().animate({marginRight:c,right:"50%"}):p(window).width()<=n.min_width?p(i).stop().css({marginRight:0,right:10}):p(i).stop().animate({marginRight:l,right:"50%"})}u(),p(i).hide().click(function(){return p("html, body").stop().animate({scrollTop:0},t.scrollSpeed,t.easingType),p("#"+t.containerHoverID,this).stop().animate({opacity:0},t.inDelay,t.easingType),!1}).prepend('<span id="'+t.containerHoverID+'"></span>').hover(function(){p(a,this).stop().animate({opacity:1},600,"linear")},function(){p(a,this).stop().animate({opacity:0},700,"linear")}),p(window).scroll(function(){var e=p(window).scrollTop();void 0===document.body.style.maxHeight&&p(i).css({position:"absolute",top:p(window).scrollTop()+p(window).height()-50}),e>t.min?p(i).css({display:"block"}):p(i).css({display:"none"})}),p(window).resize(function(){u()})}}(jQuery),$(window).on("load",function(){$().UItoTop({easingType:"easeOutQuart"})}),jQuery(function(m){m(document).ready(function(){var t=[],i=[],a=0,s="",o="",r="",l=null,c=0,u=0,p=0,d=0,f=0;m(window).scroll(function(e){var n=m(this).scrollTop();s=a<n?"down":"up",a=n}),m.fn.stickUp=function(e){m(this).addClass("stuckMenu");var n=0;if(null!=e){for(var t in e.parts)e.parts.hasOwnProperty(t)&&(i[n]=e.parts[n],n++);0==n&&console.log("error:needs arguments"),o=e.itemClass,r=e.itemHover,null!=e.topMargin?"auto"==e.topMargin?f=parseInt(m(".stuckMenu").css("margin-top")):isNaN(e.topMargin)&&0<e.topMargin.search("px")?f=parseInt(e.topMargin.replace("px","")):isNaN(parseInt(e.topMargin))?(console.log("incorrect argument, ignored."),f=0):f=parseInt(e.topMargin):f=0,l=m("."+o).size()}c=parseInt(m(this).height()),u=parseInt(m(this).css("margin-bottom")),d=parseInt(m(this).next().closest("div").css("margin-top")),p=parseInt(m(this).offset().top)},m(document).on("scroll",function(){if(varscroll=parseInt(m(document).scrollTop()),null!=l)for(var e=0;e<l;e++){t[e]=m("#"+i[e]).offset().top,"down"==s&&varscroll>t[e]-50&&varscroll<t[e]+50&&(m("."+o).removeClass(r),m("."+o+":eq("+e+")").addClass(r)),"up"==s&&(n=e,contentView=.4*m("#"+i[n]).height(),testView=t[n]-contentView,varscroll>testView?(m("."+o).removeClass(r),m("."+o+":eq("+n+")").addClass(r)):varscroll<50&&(m("."+o).removeClass(r),m("."+o+":eq(0)").addClass(r)))}var n;p<varscroll+f&&(m(".stuckMenu").addClass("isStuck"),m(".stuckMenu").next().closest("div").css({"margin-top":c+u+d+"px"},10),m(".stuckMenu").css("position","fixed"),m(".isStuck").css({top:"0px"},10,function(){})),varscroll+f<p&&(m(".stuckMenu").removeClass("isStuck"),m(".stuckMenu").next().closest("div").css({"margin-top":d+"px"},10),m(".stuckMenu").css("position","relative"))})})});