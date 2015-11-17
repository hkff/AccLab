//////////////////////////////////////////////////////////
//
//  AccLab UI : worker-aal.js
//
// Copyright (C) 2014 Walid Benghabrit
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.
//
//////////////////////////////////////////////////////////
"no use strict";
(function(c){if("undefined"==typeof c.window||!c.document){c.console=function(){var c=Array.prototype.slice.call(arguments,0);postMessage({type:"log",data:c})};c.console.error=c.console.warn=c.console.log=c.console.trace=c.console;c.window=c;c.ace=c;c.onerror=function(c,a,d,g,b){postMessage({type:"error",data:{message:c,file:a,line:d,col:g,stack:b.stack}})};c.normalizeModule=function(h,a){if(-1!==a.indexOf("!")){var d=a.split("!");return c.normalizeModule(h,d[0])+"!"+c.normalizeModule(h,d[1])}if("."==
a.charAt(0))for(d=h.split("/").slice(0,-1).join("/"),a=(d?d+"/":"")+a;-1!==a.indexOf(".")&&g!=a;){var g=a;a=a.replace(/^\.\//,"").replace(/\/\.\//,"/").replace(/[^\/]+\/\.\.\//,"")}return a};c.require=function(h,a){a||(a=h,h=null);if(!a.charAt)throw Error("worker.js require() accepts only (parentId, id) as arguments");a=c.normalizeModule(h,a);var d=c.require.modules[a];if(d)return d.initialized||(d.initialized=!0,d.exports=d.factory().exports),d.exports;d=a.split("/");if(!c.require.tlns)return console.log("unable to load "+
a);d[0]=c.require.tlns[d[0]]||d[0];d=d.join("/")+".js";return c.require.id=a,importScripts(d),c.require(h,a)};c.require.modules={};c.require.tlns={};c.define=function(h,a,d){2==arguments.length?(d=a,"string"!=typeof h&&(a=h,h=c.require.id)):1==arguments.length&&(d=h,a=[],h=c.require.id);if("function"!=typeof d)c.require.modules[h]={exports:d,initialized:!0};else{a.length||(a=["require","exports","module"]);var g=function(b){return c.require(h,b)};c.require.modules[h]={exports:{},factory:function(){var b=
this,f=d.apply(this,a.map(function(f){switch(f){case "require":return g;case "exports":return b.exports;case "module":return b;default:return g(f)}}));return f&&(b.exports=f),b}}}};c.define.amd={};c.initBaseUrls=function(c){require.tlns=c};c.initSender=function(){var h=c.require("ace/lib/event_emitter").EventEmitter,a=c.require("ace/lib/oop"),d=function(){};return function(){a.implement(this,h);this.callback=function(d,b){postMessage({type:"call",id:b,data:d})};this.emit=function(d,b){postMessage({type:"event",
name:d,data:b})}}.call(d.prototype),new d};var k=c.main=null,l=c.sender=null;c.onmessage=function(h){h=h.data;if(h.command){if(!k[h.command])throw Error("Unknown command:"+h.command);k[h.command].apply(k,h.args)}else h.init?(initBaseUrls(h.tlns),require("ace/lib/es5-shim"),l=c.sender=initSender(),h=require("ace/worker/aal_worker").MyWorker,k=c.main=new h(l)):h.event&&l&&l._signal(h.event,h.data)}}})(this);
ace.define("ace/lib/oop",["require","exports","module"],function(c,k,l){k.inherits=function(c,a){c.super_=a;c.prototype=Object.create(a.prototype,{constructor:{value:c,enumerable:!1,writable:!0,configurable:!0}})};k.mixin=function(c,a){for(var d in a)c[d]=a[d];return c};k.implement=function(c,a){k.mixin(c,a)}});
ace.define("ace/lib/event_emitter",["require","exports","module"],function(c,k,l){c={};var h=function(){this.propagationStopped=!0},a=function(){this.defaultPrevented=!0};c._emit=c._dispatchEvent=function(d,g){this._eventRegistry||(this._eventRegistry={});this._defaultHandlers||(this._defaultHandlers={});var b=this._eventRegistry[d]||[],f=this._defaultHandlers[d];if(b.length||f){"object"==typeof g&&g||(g={});g.type||(g.type=d);g.stopPropagation||(g.stopPropagation=h);g.preventDefault||(g.preventDefault=
a);for(var b=b.slice(),e=0;e<b.length&&(b[e](g,this),!g.propagationStopped);e++);if(f&&!g.defaultPrevented)return f(g,this)}};c._signal=function(d,a){var b=(this._eventRegistry||{})[d];if(b)for(var b=b.slice(),f=0;f<b.length;f++)b[f](a,this)};c.once=function(d,a){var b=this;a&&this.addEventListener(d,function e(){b.removeEventListener(d,e);a.apply(null,arguments)})};c.setDefaultHandler=function(d,a){var b=this._defaultHandlers;b||(b=this._defaultHandlers={_disabled_:{}});if(b[d]){var f=b[d],e=b._disabled_[d];
e||(b._disabled_[d]=e=[]);e.push(f);f=e.indexOf(a);-1!=f&&e.splice(f,1)}b[d]=a};c.removeDefaultHandler=function(d,a){var b=this._defaultHandlers;if(b){var f=b._disabled_[d];b[d]==a?f&&this.setDefaultHandler(d,f.pop()):f&&(b=f.indexOf(a),-1!=b&&f.splice(b,1))}};c.on=c.addEventListener=function(d,a,b){this._eventRegistry=this._eventRegistry||{};var f=this._eventRegistry[d];return f||(f=this._eventRegistry[d]=[]),-1==f.indexOf(a)&&f[b?"unshift":"push"](a),a};c.off=c.removeListener=c.removeEventListener=
function(d,a){this._eventRegistry=this._eventRegistry||{};var b=this._eventRegistry[d];if(b){var f=b.indexOf(a);-1!==f&&b.splice(f,1)}};c.removeAllListeners=function(d){this._eventRegistry&&(this._eventRegistry[d]=[])};k.EventEmitter=c});
ace.define("ace/range",["require","exports","module"],function(c,k,l){var h=function(a,d,g,b){this.start={row:a,column:d};this.end={row:g,column:b}};(function(){this.isEqual=function(a){return this.start.row===a.start.row&&this.end.row===a.end.row&&this.start.column===a.start.column&&this.end.column===a.end.column};this.toString=function(){return"Range: ["+this.start.row+"/"+this.start.column+"] -> ["+this.end.row+"/"+this.end.column+"]"};this.contains=function(a,d){return 0==this.compare(a,d)};this.compareRange=
function(a){var d,g=a.end;a=a.start;return d=this.compare(g.row,g.column),1==d?(d=this.compare(a.row,a.column),1==d?2:0==d?1:0):-1==d?-2:(d=this.compare(a.row,a.column),-1==d?-1:1==d?42:0)};this.comparePoint=function(a){return this.compare(a.row,a.column)};this.containsRange=function(a){return 0==this.comparePoint(a.start)&&0==this.comparePoint(a.end)};this.intersects=function(a){a=this.compareRange(a);return-1==a||0==a||1==a};this.isEnd=function(a,d){return this.end.row==a&&this.end.column==d};this.isStart=
function(a,d){return this.start.row==a&&this.start.column==d};this.setStart=function(a,d){"object"==typeof a?(this.start.column=a.column,this.start.row=a.row):(this.start.row=a,this.start.column=d)};this.setEnd=function(a,d){"object"==typeof a?(this.end.column=a.column,this.end.row=a.row):(this.end.row=a,this.end.column=d)};this.inside=function(a,d){return 0==this.compare(a,d)?this.isEnd(a,d)||this.isStart(a,d)?!1:!0:!1};this.insideStart=function(a,d){return 0==this.compare(a,d)?this.isEnd(a,d)?!1:
!0:!1};this.insideEnd=function(a,d){return 0==this.compare(a,d)?this.isStart(a,d)?!1:!0:!1};this.compare=function(a,d){return this.isMultiLine()||a!==this.start.row?a<this.start.row?-1:a>this.end.row?1:this.start.row===a?d>=this.start.column?0:-1:this.end.row===a?d<=this.end.column?0:1:0:d<this.start.column?-1:d>this.end.column?1:0};this.compareStart=function(a,d){return this.start.row==a&&this.start.column==d?-1:this.compare(a,d)};this.compareEnd=function(a,d){return this.end.row==a&&this.end.column==
d?1:this.compare(a,d)};this.compareInside=function(a,d){return this.end.row==a&&this.end.column==d?1:this.start.row==a&&this.start.column==d?-1:this.compare(a,d)};this.clipRows=function(a,d){if(this.end.row>d)var g={row:d+1,column:0};else this.end.row<a&&(g={row:a,column:0});if(this.start.row>d)var b={row:d+1,column:0};else this.start.row<a&&(b={row:a,column:0});return h.fromPoints(b||this.start,g||this.end)};this.extend=function(a,d){var g=this.compare(a,d);if(0==g)return this;if(-1==g)var b={row:a,
column:d};else var f={row:a,column:d};return h.fromPoints(b||this.start,f||this.end)};this.isEmpty=function(){return this.start.row===this.end.row&&this.start.column===this.end.column};this.isMultiLine=function(){return this.start.row!==this.end.row};this.clone=function(){return h.fromPoints(this.start,this.end)};this.collapseRows=function(){return 0==this.end.column?new h(this.start.row,0,Math.max(this.start.row,this.end.row-1),0):new h(this.start.row,0,this.end.row,0)};this.toScreenRange=function(a){var d=
a.documentToScreenPosition(this.start);a=a.documentToScreenPosition(this.end);return new h(d.row,d.column,a.row,a.column)};this.moveBy=function(a,d){this.start.row+=a;this.start.column+=d;this.end.row+=a;this.end.column+=d}}).call(h.prototype);h.fromPoints=function(a,d){return new h(a.row,a.column,d.row,d.column)};h.comparePoints=function(a,d){return a.row-d.row||a.column-d.column};h.comparePoints=function(a,d){return a.row-d.row||a.column-d.column};k.Range=h});
ace.define("ace/anchor",["require","exports","module","ace/lib/oop","ace/lib/event_emitter"],function(c,k,l){var h=c("./lib/oop"),a=c("./lib/event_emitter").EventEmitter;c=k.Anchor=function(d,a,b){this.$onChange=this.onChange.bind(this);this.attach(d);"undefined"==typeof b?this.setPosition(a.row,a.column):this.setPosition(a,b)};(function(){h.implement(this,a);this.getPosition=function(){return this.$clipPositionToDocument(this.row,this.column)};this.getDocument=function(){return this.document};this.$insertRight=
!1;this.onChange=function(d){d=d.data;var a=d.range;if(!(a.start.row==a.end.row&&a.start.row!=this.row||a.start.row>this.row||a.start.row==this.row&&a.start.column>this.column)){var b=this.row,f=this.column,e=a.start,a=a.end;"insertText"===d.action?e.row===b&&e.column<=f?e.column===f&&this.$insertRight||(e.row===a.row?f+=a.column-e.column:(f-=e.column,b+=a.row-e.row)):e.row!==a.row&&e.row<b&&(b+=a.row-e.row):"insertLines"===d.action?(e.row!==b||0!==f||!this.$insertRight)&&e.row<=b&&(b+=a.row-e.row):
"removeText"===d.action?e.row===b&&e.column<f?a.column>=f?f=e.column:f=Math.max(0,f-(a.column-e.column)):e.row!==a.row&&e.row<b?(a.row===b&&(f=Math.max(0,f-a.column)+e.column),b-=a.row-e.row):a.row===b&&(b-=a.row-e.row,f=Math.max(0,f-a.column)+e.column):"removeLines"==d.action&&e.row<=b&&(a.row<=b?b-=a.row-e.row:(b=e.row,f=0));this.setPosition(b,f,!0)}};this.setPosition=function(d,a,b){var f;b?f={row:d,column:a}:f=this.$clipPositionToDocument(d,a);if(this.row!=f.row||this.column!=f.column)d={row:this.row,
column:this.column},this.row=f.row,this.column=f.column,this._signal("change",{old:d,value:f})};this.detach=function(){this.document.removeEventListener("change",this.$onChange)};this.attach=function(d){this.document=d||this.document;this.document.on("change",this.$onChange)};this.$clipPositionToDocument=function(d,a){var b={};return d>=this.document.getLength()?(b.row=Math.max(0,this.document.getLength()-1),b.column=this.document.getLine(b.row).length):0>d?(b.row=0,b.column=0):(b.row=d,b.column=
Math.min(this.document.getLine(b.row).length,Math.max(0,a))),0>a&&(b.column=0),b}}).call(c.prototype)});
ace.define("ace/document","require exports module ace/lib/oop ace/lib/event_emitter ace/range ace/anchor".split(" "),function(c,k,l){var h=c("./lib/oop"),a=c("./lib/event_emitter").EventEmitter,d=c("./range").Range,g=c("./anchor").Anchor;c=function(b){this.$lines=[];0===b.length?this.$lines=[""]:Array.isArray(b)?this._insertLines(0,b):this.insert({row:0,column:0},b)};(function(){h.implement(this,a);this.setValue=function(b){var f=this.getLength();this.remove(new d(0,0,f,this.getLine(f-1).length));
this.insert({row:0,column:0},b)};this.getValue=function(){return this.getAllLines().join(this.getNewLineCharacter())};this.createAnchor=function(b,f){return new g(this,b,f)};0==="aaa".split(/a/).length?this.$split=function(b){return b.replace(/\r\n|\r/g,"\n").split("\n")}:this.$split=function(b){return b.split(/\r\n|\r|\n/)};this.$detectNewLine=function(b){this.$autoNewLine=(b=b.match(/^.*?(\r\n|\r|\n)/m))?b[1]:"\n";this._signal("changeNewLineMode")};this.getNewLineCharacter=function(){switch(this.$newLineMode){case "windows":return"\r\n";
case "unix":return"\n";default:return this.$autoNewLine||"\n"}};this.$autoNewLine="";this.$newLineMode="auto";this.setNewLineMode=function(b){this.$newLineMode!==b&&(this.$newLineMode=b,this._signal("changeNewLineMode"))};this.getNewLineMode=function(){return this.$newLineMode};this.isNewLine=function(b){return"\r\n"==b||"\r"==b||"\n"==b};this.getLine=function(b){return this.$lines[b]||""};this.getLines=function(b,f){return this.$lines.slice(b,f+1)};this.getAllLines=function(){return this.getLines(0,
this.getLength())};this.getLength=function(){return this.$lines.length};this.getTextRange=function(b){if(b.start.row==b.end.row)return this.getLine(b.start.row).substring(b.start.column,b.end.column);var f=this.getLines(b.start.row,b.end.row);f[0]=(f[0]||"").substring(b.start.column);var d=f.length-1;return b.end.row-b.start.row==d&&(f[d]=f[d].substring(0,b.end.column)),f.join(this.getNewLineCharacter())};this.$clipPosition=function(b){var f=this.getLength();return b.row>=f?(b.row=Math.max(0,f-1),
b.column=this.getLine(f-1).length):0>b.row&&(b.row=0),b};this.insert=function(b,f){if(!f||0===f.length)return b;b=this.$clipPosition(b);1>=this.getLength()&&this.$detectNewLine(f);var d=this.$split(f),a=d.splice(0,1)[0],c=0==d.length?null:d.splice(d.length-1,1)[0];return b=this.insertInLine(b,a),null!==c&&(b=this.insertNewLine(b),b=this._insertLines(b.row,d),b=this.insertInLine(b,c||"")),b};this.insertLines=function(b,d){return b>=this.getLength()?this.insert({row:b,column:0},"\n"+d.join("\n")):this._insertLines(Math.max(b,
0),d)};this._insertLines=function(b,f){if(0==f.length)return{row:b,column:0};for(;2E4<f.length;){var a=this._insertLines(b,f.slice(0,2E4));f=f.slice(2E4);b=a.row}a=[b,0];a.push.apply(a,f);this.$lines.splice.apply(this.$lines,a);a=new d(b,0,b+f.length,0);return this._signal("change",{data:{action:"insertLines",range:a,lines:f}}),a.end};this.insertNewLine=function(b){b=this.$clipPosition(b);var a=this.$lines[b.row]||"";this.$lines[b.row]=a.substring(0,b.column);this.$lines.splice(b.row+1,0,a.substring(b.column,
a.length));a={row:b.row+1,column:0};b={action:"insertText",range:d.fromPoints(b,a),text:this.getNewLineCharacter()};return this._signal("change",{data:b}),a};this.insertInLine=function(b,a){if(0==a.length)return b;var e=this.$lines[b.row]||"";this.$lines[b.row]=e.substring(0,b.column)+a+e.substring(b.column);var e={row:b.row,column:b.column+a.length},c={action:"insertText",range:d.fromPoints(b,e),text:a};return this._signal("change",{data:c}),e};this.remove=function(b){b instanceof d||(b=d.fromPoints(b.start,
b.end));b.start=this.$clipPosition(b.start);b.end=this.$clipPosition(b.end);if(b.isEmpty())return b.start;var a=b.start.row,e=b.end.row;if(b.isMultiLine()){var c=0==b.start.column?a:a+1,g=e-1;0<b.end.column&&this.removeInLine(e,0,b.end.column);g>=c&&this._removeLines(c,g);c!=a&&(this.removeInLine(a,b.start.column,this.getLine(a).length),this.removeNewLine(b.start.row))}else this.removeInLine(a,b.start.column,b.end.column);return b.start};this.removeInLine=function(b,a,e){if(a!=e){var c=new d(b,a,
b,e),g=this.getLine(b),h=g.substring(a,e);a=g.substring(0,a)+g.substring(e,g.length);this.$lines.splice(b,1,a);return this._signal("change",{data:{action:"removeText",range:c,text:h}}),c.start}};this.removeLines=function(b,a){return 0>b||a>=this.getLength()?this.remove(new d(b,0,a+1,0)):this._removeLines(b,a)};this._removeLines=function(b,a){var e=new d(b,0,a+1,0),c=this.$lines.splice(b,a-b+1),e={action:"removeLines",range:e,nl:this.getNewLineCharacter(),lines:c};return this._signal("change",{data:e}),
c};this.removeNewLine=function(b){var a=this.getLine(b),e=this.getLine(b+1),c=new d(b,a.length,b+1,0);this.$lines.splice(b,2,a+e);b={action:"removeText",range:c,text:this.getNewLineCharacter()};this._signal("change",{data:b})};this.replace=function(b,a){b instanceof d||(b=d.fromPoints(b.start,b.end));if(0==a.length&&b.isEmpty())return b.start;if(a==this.getTextRange(b))return b.end;this.remove(b);return a?this.insert(b.start,a):b.start};this.applyDeltas=function(b){for(var a=0;a<b.length;a++){var c=
b[a],g=d.fromPoints(c.range.start,c.range.end);"insertLines"==c.action?this.insertLines(g.start.row,c.lines):"insertText"==c.action?this.insert(g.start,c.text):"removeLines"==c.action?this._removeLines(g.start.row,g.end.row-1):"removeText"==c.action&&this.remove(g)}};this.revertDeltas=function(b){for(var a=b.length-1;0<=a;a--){var c=b[a],g=d.fromPoints(c.range.start,c.range.end);"insertLines"==c.action?this._removeLines(g.start.row,g.end.row-1):"insertText"==c.action?this.remove(g):"removeLines"==
c.action?this._insertLines(g.start.row,c.lines):"removeText"==c.action&&this.insert(g.start,c.text)}};this.indexToPosition=function(b,a){for(var d=this.$lines||this.getAllLines(),c=this.getNewLineCharacter().length,g=a||0,h=d.length;g<h;g++)if(b-=d[g].length+c,0>b)return{row:g,column:b+d[g].length+c};return{row:h-1,column:d[h-1].length}};this.positionToIndex=function(b,a){for(var d=this.$lines||this.getAllLines(),c=this.getNewLineCharacter().length,g=0,h=Math.min(b.row,d.length),k=a||0;k<h;++k)g+=
d[k].length+c;return g+b.column}}).call(c.prototype);k.Document=c});
ace.define("ace/lib/lang",["require","exports","module"],function(c,k,l){k.last=function(a){return a[a.length-1]};k.stringReverse=function(a){return a.split("").reverse().join("")};k.stringRepeat=function(a,c){for(var b="";0<c;)if(c&1&&(b+=a),c>>=1)a+=a;return b};var h=/^\s\s*/,a=/\s\s*$/;k.stringTrimLeft=function(a){return a.replace(h,"")};k.stringTrimRight=function(d){return d.replace(a,"")};k.copyObject=function(a){var c={},b;for(b in a)c[b]=a[b];return c};k.copyArray=function(a){for(var c=[],
b=0,f=a.length;b<f;b++)a[b]&&"object"==typeof a[b]?c[b]=this.copyObject(a[b]):c[b]=a[b];return c};k.deepCopy=function g(b){if("object"!=typeof b||!b)return b;var a;if(Array.isArray(b)){a=[];for(var c=0;c<b.length;c++)a[c]=g(b[c]);return a}a=b.constructor;if(a===RegExp)return b;a=a();for(c in b)a[c]=g(b[c]);return a};k.arrayToMap=function(a){for(var b={},c=0;c<a.length;c++)b[a[c]]=1;return b};k.createMap=function(a){var b=Object.create(null),c;for(c in a)b[c]=a[c];return b};k.arrayRemove=function(a,
b){for(var c=0;c<=a.length;c++)b===a[c]&&a.splice(c,1)};k.escapeRegExp=function(a){return a.replace(/([.*+?^${}()|[\]\/\\])/g,"\\$1")};k.escapeHTML=function(a){return a.replace(/&/g,"&#38;").replace(/"/g,"&#34;").replace(/'/g,"&#39;").replace(/</g,"&#60;")};k.getMatchOffsets=function(a,b){var c=[];return a.replace(b,function(a){c.push({offset:arguments[arguments.length-2],length:a.length})}),c};k.deferredCall=function(a){var b=null,c=function(){b=null;a()},e=function(a){return e.cancel(),b=setTimeout(c,
a||0),e};return e.schedule=e,e.call=function(){return this.cancel(),a(),e},e.cancel=function(){return clearTimeout(b),b=null,e},e.isPending=function(){return b},e};k.delayedCall=function(a,b){var c=null,e=function(){c=null;a()},h=function(a){null==c&&(c=setTimeout(e,a||b))};return h.delay=function(a){c&&clearTimeout(c);c=setTimeout(e,a||b)},h.schedule=h,h.call=function(){this.cancel();a()},h.cancel=function(){c&&clearTimeout(c);c=null},h.isPending=function(){return c},h}});
ace.define("ace/worker/mirror",["require","exports","module","ace/document","ace/lib/lang"],function(c,k,l){var h=c("../document").Document,a=c("../lib/lang");c=k.Mirror=function(d){this.sender=d;var c=this.doc=new h(""),b=this.deferredUpdate=a.delayedCall(this.onUpdate.bind(this)),f=this;d.on("change",function(a){c.applyDeltas(a.data);if(f.$timeout)return b.schedule(f.$timeout);f.onUpdate()})};(function(){this.$timeout=500;this.setTimeout=function(a){this.$timeout=a};this.setValue=function(a){this.doc.setValue(a);
this.deferredUpdate.schedule(this.$timeout)};this.getValue=function(a){this.sender.callback(this.doc.getValue(),a)};this.onUpdate=function(){};this.isPending=function(){return this.deferredUpdate.isPending()}}).call(c.prototype)});
ace.define("ace/lib/es5-shim",["require","exports","module"],function(c,k,l){function h(){}function a(a){try{return Object.defineProperty(a,"sentinel",{}),"sentinel"in a}catch(b){}}function d(a){return a=+a,a!==a?a=0:0!==a&&a!==1/0&&a!==-1/0&&(a=(0<a||-1)*Math.floor(Math.abs(a))),a}Function.prototype.bind||(Function.prototype.bind=function(a){var d=this;if("function"!=typeof d)throw new TypeError("Function.prototype.bind called on incompatible "+d);var c=b.call(arguments,1),f=function(){if(this instanceof
f){var e=d.apply(this,c.concat(b.call(arguments)));return Object(e)===e?e:this}return d.apply(a,c.concat(b.call(arguments)))};return d.prototype&&(h.prototype=d.prototype,f.prototype=new h,h.prototype=null),f});c=Function.prototype.call;var g=Object.prototype,b=Array.prototype.slice,f=c.bind(g.toString),e=c.bind(g.hasOwnProperty),w,x,r,t,q;if(q=e(g,"__defineGetter__"))w=c.bind(g.__defineGetter__),x=c.bind(g.__defineSetter__),r=c.bind(g.__lookupGetter__),t=c.bind(g.__lookupSetter__);if(2!=[1,2].splice(0).length)if(function(){function a(b){b=
Array(b+2);return b[0]=b[1]=0,b}var b=[],d;b.splice.apply(b,a(20));b.splice.apply(b,a(26));d=b.length;b.splice(5,0,"XXX");d+1==b.length;if(d+1==b.length)return!0}()){var A=Array.prototype.splice;Array.prototype.splice=function(a,d){return arguments.length?A.apply(this,[void 0===a?0:a,void 0===d?this.length-a:d].concat(b.call(arguments,2))):[]}}else Array.prototype.splice=function(a,d){var c=this.length;0<a?a>c&&(a=c):void 0==a?a=0:0>a&&(a=Math.max(c+a,0));a+d<c||(d=c-a);var f=this.slice(a,a+d),e=
b.call(arguments,2),h=e.length;if(a===c)h&&this.push.apply(this,e);else{var g=Math.min(d,c-a),k=a+g,l=k+h-g,m=c-k,c=c-g;if(l<k)for(g=0;g<m;++g)this[l+g]=this[k+g];else if(l>k)for(g=m;g--;)this[l+g]=this[k+g];if(h&&a===c)this.length=c,this.push.apply(this,e);else for(this.length=c+h,g=0;g<h;++g)this[a+g]=e[g]}return f};Array.isArray||(Array.isArray=function(a){return"[object Array]"==f(a)});c=Object("a");var m="a"!=c[0]||!(0 in c);Array.prototype.forEach||(Array.prototype.forEach=function(a,b){var d=
n(this),c=m&&"[object String]"==f(this)?this.split(""):d,g=-1,e=c.length>>>0;if("[object Function]"!=f(a))throw new TypeError;for(;++g<e;)g in c&&a.call(b,c[g],g,d)});Array.prototype.map||(Array.prototype.map=function(a,b){var d=n(this),c=m&&"[object String]"==f(this)?this.split(""):d,g=c.length>>>0,e=Array(g);if("[object Function]"!=f(a))throw new TypeError(a+" is not a function");for(var h=0;h<g;h++)h in c&&(e[h]=a.call(b,c[h],h,d));return e});Array.prototype.filter||(Array.prototype.filter=function(a,
b){var d=n(this),c=m&&"[object String]"==f(this)?this.split(""):d,g=c.length>>>0,e=[],h;if("[object Function]"!=f(a))throw new TypeError(a+" is not a function");for(var k=0;k<g;k++)k in c&&(h=c[k],a.call(b,h,k,d)&&e.push(h));return e});Array.prototype.every||(Array.prototype.every=function(a,b){var d=n(this),c=m&&"[object String]"==f(this)?this.split(""):d,g=c.length>>>0;if("[object Function]"!=f(a))throw new TypeError(a+" is not a function");for(var e=0;e<g;e++)if(e in c&&!a.call(b,c[e],e,d))return!1;
return!0});Array.prototype.some||(Array.prototype.some=function(a,b){var d=n(this),c=m&&"[object String]"==f(this)?this.split(""):d,g=c.length>>>0;if("[object Function]"!=f(a))throw new TypeError(a+" is not a function");for(var e=0;e<g;e++)if(e in c&&a.call(b,c[e],e,d))return!0;return!1});Array.prototype.reduce||(Array.prototype.reduce=function(a){var b=n(this),c=m&&"[object String]"==f(this)?this.split(""):b,d=c.length>>>0;if("[object Function]"!=f(a))throw new TypeError(a+" is not a function");
if(!d&&1==arguments.length)throw new TypeError("reduce of empty array with no initial value");var e=0,g;if(2<=arguments.length)g=arguments[1];else{do{if(e in c){g=c[e++];break}if(++e>=d)throw new TypeError("reduce of empty array with no initial value");}while(1)}for(;e<d;e++)e in c&&(g=a.call(void 0,g,c[e],e,b));return g});Array.prototype.reduceRight||(Array.prototype.reduceRight=function(a){var b=n(this),c=m&&"[object String]"==f(this)?this.split(""):b,d=c.length>>>0;if("[object Function]"!=f(a))throw new TypeError(a+
" is not a function");if(!d&&1==arguments.length)throw new TypeError("reduceRight of empty array with no initial value");var e,d=d-1;if(2<=arguments.length)e=arguments[1];else{do{if(d in c){e=c[d--];break}if(0>--d)throw new TypeError("reduceRight of empty array with no initial value");}while(1)}do d in this&&(e=a.call(void 0,e,c[d],d,b));while(d--);return e});Array.prototype.indexOf&&-1==[0,1].indexOf(1,2)||(Array.prototype.indexOf=function(a){var b=m&&"[object String]"==f(this)?this.split(""):n(this),
c=b.length>>>0;if(!c)return-1;var e=0;1<arguments.length&&(e=d(arguments[1]));for(e=0<=e?e:Math.max(0,c+e);e<c;e++)if(e in b&&b[e]===a)return e;return-1});Array.prototype.lastIndexOf&&-1==[0,1].lastIndexOf(0,-3)||(Array.prototype.lastIndexOf=function(a){var b=m&&"[object String]"==f(this)?this.split(""):n(this),c=b.length>>>0;if(!c)return-1;var e=c-1;1<arguments.length&&(e=Math.min(e,d(arguments[1])));for(e=0<=e?e:c-Math.abs(e);0<=e;e--)if(e in b&&a===b[e])return e;return-1});Object.getPrototypeOf||
(Object.getPrototypeOf=function(a){return a.__proto__||(a.constructor?a.constructor.prototype:g)});Object.getOwnPropertyDescriptor||(Object.getOwnPropertyDescriptor=function(a,b){if("object"!=typeof a&&"function"!=typeof a||null===a)throw new TypeError("Object.getOwnPropertyDescriptor called on a non-object: "+a);if(e(a,b)){var c,d,f;c={enumerable:!0,configurable:!0};if(q){var h=a.__proto__;a.__proto__=g;d=r(a,b);f=t(a,b);a.__proto__=h;if(d||f)return d&&(c.get=d),f&&(c.set=f),c}return c.value=a[b],
c}});Object.getOwnPropertyNames||(Object.getOwnPropertyNames=function(a){return Object.keys(a)});if(!Object.create){var u;null===Object.prototype.__proto__?u=function(){return{__proto__:null}}:u=function(){var a={},b;for(b in a)a[b]=null;return a.constructor=a.hasOwnProperty=a.propertyIsEnumerable=a.isPrototypeOf=a.toLocaleString=a.toString=a.valueOf=a.__proto__=null,a};Object.create=function(a,b){var c;if(null===a)c=u();else{if("object"!=typeof a)throw new TypeError("typeof prototype["+typeof a+
"] != 'object'");c=function(){};c.prototype=a;c=new c;c.__proto__=a}return void 0!==b&&Object.defineProperties(c,b),c}}if(Object.defineProperty&&(c=a({}),k="undefined"==typeof document||a(document.createElement("div")),!c||!k))var v=Object.defineProperty;if(!Object.defineProperty||v)Object.defineProperty=function(a,b,c){if("object"!=typeof a&&"function"!=typeof a||null===a)throw new TypeError("Object.defineProperty called on non-object: "+a);if("object"!=typeof c&&"function"!=typeof c||null===c)throw new TypeError("Property description must be an object: "+
c);if(v)try{return v.call(Object,a,b,c)}catch(d){}if(e(c,"value"))if(q&&(r(a,b)||t(a,b))){var f=a.__proto__;a.__proto__=g;delete a[b];a[b]=c.value;a.__proto__=f}else a[b]=c.value;else{if(!q)throw new TypeError("getters & setters can not be defined on this javascript engine");e(c,"get")&&w(a,b,c.get);e(c,"set")&&x(a,b,c.set)}return a};Object.defineProperties||(Object.defineProperties=function(a,b){for(var c in b)e(b,c)&&Object.defineProperty(a,c,b[c]);return a});Object.seal||(Object.seal=function(a){return a});
Object.freeze||(Object.freeze=function(a){return a});try{Object.freeze(function(){})}catch(E){Object.freeze=function(a){return function(b){return"function"==typeof b?b:a(b)}}(Object.freeze)}Object.preventExtensions||(Object.preventExtensions=function(a){return a});Object.isSealed||(Object.isSealed=function(a){return!1});Object.isFrozen||(Object.isFrozen=function(a){return!1});Object.isExtensible||(Object.isExtensible=function(a){if(Object(a)===a)throw new TypeError;for(var b="";e(a,b);)b+="?";a[b]=
!0;var c=e(a,b);return delete a[b],c});if(!Object.keys){var y=!0,z="toString toLocaleString valueOf hasOwnProperty isPrototypeOf propertyIsEnumerable constructor".split(" "),B=z.length,p;for(p in{toString:null})y=!1;Object.keys=function(a){if("object"!=typeof a&&"function"!=typeof a||null===a)throw new TypeError("Object.keys called on a non-object");var b=[],c;for(c in a)e(a,c)&&b.push(c);if(y)for(c=0;c<B;c++){var d=z[c];e(a,d)&&b.push(d)}return b}}Date.now||(Date.now=function(){return(new Date).getTime()});
p="\t\n\x0B\f\r \u00a0\u1680\u180e\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000\u2028\u2029\ufeff";if(!String.prototype.trim||p.trim()){p="["+p+"]";var C=new RegExp("^"+p+p+"*"),D=new RegExp(p+p+"*$");String.prototype.trim=function(){return String(this).replace(C,"").replace(D,"")}}var n=function(a){if(null==a)throw new TypeError("can't convert "+a+" to object");return Object(a)}});


//=======================================================================//
//                             AAL Worker                                //
//=======================================================================//

// Loading antlr4
var ace_require = require;
require = undefined;
var Honey = { 'requirePath': ['/ui/libs/'] };
importScripts("../../aal/require.js");
var antlr4_require = require;
require = ace_require;
var antlr4, aal;
try {
    require = antlr4_require;
    antlr4 = require('antlr4/index');
    aal = require('aal/index');
} finally {
    require = ace_require;
}

/**
 * Class for gathering errors and posting them to ACE editor
 */
var AnnotatingErrorListener = function(annotations) {
    antlr4.error.ErrorListener.call(this);
    this.annotations = annotations;
    return this;
};

var DEBUG = true;

AnnotatingErrorListener.prototype = Object.create(antlr4.error.ErrorListener.prototype);
AnnotatingErrorListener.prototype.constructor = AnnotatingErrorListener;
AnnotatingErrorListener.prototype.syntaxError = function(recognizer, offendingSymbol, line, column, msg, e) {
    var parser = recognizer._ctx.parser,
        tokens = parser.getTokenStream().tokens;
    // Push the annotation
    var res = error_linter(msg, tokens, offendingSymbol) +
        "\n\nDEBUG :" +
        "\ntoken -1 : " + tokens[tokens.length-1].toString() +
        "\ntoken -2 : " + tokens[tokens.length-2].toString() +
        "\ntoken -3 : " + tokens[tokens.length-3].toString() +
        "\nMsg : " + msg +
        "\nOffendingSymbol : " + offendingSymbol;
    this.annotations.push({row: line - 1, column: column, text: res, type: "error"});
};


/***************************************
 *  Syntax error linter
 ***************************************/
var error_rules =
{
    // "extraneous input <tokenName> expecting  <expectedTokens>"
    "rule1" : {"msg": "extraneous input ",          "level": "error", "hint": "Incomplete definition"},

    // "mismatched input <tokenName> expecting <expectedTokens>"
    "rule2" : {"msg": "mismatched input ",          "level": "error", "hint": "Incomplete definition"},

    // "missing <tokenName> at <input>"
    "rule3" : {"msg": "missing ",                   "level": "error", "hint": "Incomplete definition"},

    // "no viable alternative at <input>"
    "rule4" : {"msg": "no viable alternative at ",  "level": "error", "hint": "Incomplete definition"}

};

var handleANTLRmsg = function(msg) {
    var rule, givenToken, expectedTokens, expattern = null;

    // Checking rule1 / rule2
    rule = (msg.startsWith(error_rules["rule1"].msg))?error_rules["rule1"]:null;
    rule = (msg.startsWith(error_rules["rule2"].msg))?error_rules["rule2"]:rule;

    if(rule != null) {
        expattern = msg.indexOf("expecting");
        givenToken = msg.substring(rule.msg.length, expattern - 1);
        expectedTokens = msg.substring(expattern + 10, msg.length).split(",");
        if(expectedTokens.length > 1) {
            expectedTokens[0] = expectedTokens[0].substring(1);
            expectedTokens[expectedTokens.length-1] = expectedTokens[expectedTokens.length-1]
                .substring(0, expectedTokens[expectedTokens.length-1].length-1);
        }
        return {"rule": (msg.startsWith(error_rules["rule1"].msg))?1:2,
                "givenToken": givenToken, "expectedTokens": expectedTokens, "msg": msg};
    }

    // Checking rule3
    rule = (msg.startsWith(error_rules["rule3"].msg))?error_rules["rule3"]:null;
    if(rule != null) {
        expattern = msg.indexOf("at");
        expectedTokens = msg.substring(rule.msg.length, expattern - 1);
        givenToken= msg.substring(expattern + 3, msg.length);
        return {"rule": 3, "givenToken": givenToken, "expectedTokens": expectedTokens, "msg": msg};
    }

    // Checking rule4
    rule = (msg.startsWith(error_rules["rule4"].msg))?error_rules["rule4"]:null;
    if(rule != null) {
        givenToken = msg.substring(rule.msg.length, msg.length);
        return {"rule": 4, "givenToken": givenToken, "expectedTokens": [], "msg": msg};
    }

    return {"rule": 0, "givenToken": givenToken, "expectedTokens": expectedTokens, "msg": msg};
};


var findToken = function(tokenName, tokens, options) {
    if(!options) options = {};
    if(!options.start) options.start = tokens.length - 1;
    if(!options.end)   options.end = 0;
    options.end = (tokens.length > options.end)? options.start - options.end : 0;

    for(var i=options.start; i>=options.end; i--) {
        if(tokens[i].text === tokenName)
            return true;
    }
    return false;
};


/**
 * Syntax error linter
 * @param msg
 * @param tokens
 * @param offendingSymbol
 * @returns {*}
 */
var error_linter = function(msg, tokens, offendingSymbol) {
    var res = "";
    var ant = handleANTLRmsg(msg);

    res = "token -1 : " + tokens[tokens.length-1].toString() +
        "\ntoken -2 : " + tokens[tokens.length-2].toString() +
        "\ntoken -3 : " + tokens[tokens.length-3].toString() +
        "\nMsg : " + ant.msg +
        "\nExpected : " + ant.expectedTokens + "\nGiven : " + ant.givenToken +
        "\nOffendingSymbol : " + offendingSymbol;

    // Matching rules
    switch(ant.rule) {
        //=============================================================
        // "extraneous input <tokenName> expecting  <expectedTokens>"
        //=============================================================
        case 1:
            // RULE 1.1 (Accuracy 90%) : Comment
            if(findToken("/", tokens, {"end": 5}) && ant.givenToken === "'/'")
                return 'Maybe your are missing a / before your comment \nTo comment a line use : // ........';

            // RULE 1.2 (Accuracy ??%) : AGENT declaration missing PROVIDED services
            if(findToken("AGENT", tokens, {"end": 15}) && ant.expectedTokens.indexOf("'PROVIDED'") != -1)
                return 'PROVIDED services are missing in your declaration \nHere is how to declare an agent : \n' +
                    'AGENT name TYPES(type1 type2 ...) REQUIRED(service1 service2 ...) PROVIDED(s1 s2 ...)';

            // RULE 1.3 (Accuracy ??%) : AGENT declaration missing REQUIRED services
            if(findToken("AGENT", tokens, {"end": 15}) && ant.expectedTokens.indexOf("'REQUIRED'") != -1)
                return 'REQUIRED services are missing in your declaration \nHere is how to declare an agent : \n' +
                    'AGENT name TYPES(type1 type2 ...) REQUIRED(service1 service2 ...) PROVIDED(service1 service2 ...)';

            break;

        //=============================================================
        // "mismatched input <tokenName> expecting <expectedTokens>"
        //=============================================================
        case 2:
            // RULE 2.1 (Accuracy ??%) : AGENT declaration missing PROVIDED services
            if(findToken("AGENT", tokens, {"end": 15}) && ant.expectedTokens.indexOf("'PROVIDED'") != -1)
                return 'PROVIDED services are missing in your declaration \nHere is how to declare an agent : \n' +
                    'AGENT name TYPES(type1 type2 ...) REQUIRED(service1 service2 ...) PROVIDED(s1 s2 ...)';

            // RULE 2.2 (Accuracy ??%) : AGENT declaration missing REQUIRED services
            if(findToken("AGENT", tokens, {"end": 15}) && ant.expectedTokens.indexOf("'REQUIRED'") != -1)
                return 'REQUIRED services are missing in your declaration \nHere is how to declare an agent : \n' +
                    'AGENT name TYPES(type1 type2 ...) REQUIRED(service1 service2 ...) PROVIDED(service1 service2 ...)';

            break;

        //=============================================================
        // "missing <tokenName> at <token>"
        //=============================================================
        case 3:
            // RULE 3.1 (Accuracy ??%) : Load
            if(findToken("LOAD", tokens, {"end": 5}) && ant.expectedTokens === "null")
                return 'Maybe your are missing double quotes " "\nHere how to load a library : LOAD "lib_path"';

            // RULE 3.2 (Accuracy ??%) : Clause
            if(findToken("CLAUSE", tokens, {"end": 10}) && ant.expectedTokens === "'('")
                return 'Maybe your are missing a parenthesis ( after clause name \nHere how declare a clause :\n' +
                    'CLAUSE clause_name ( expr )';

            break;

        //=============================================================
        // "no viable alternative at <input>"
        //=============================================================
        case 4:
            // RULE 4.1 (Accuracy 20%) : Missing the right-hand expression in a comparison of an IF_THEN condition
            if((findToken("==", tokens, {"start": offendingSymbol.tokenIndex+1, "end": 3}) ||
                findToken("!=", tokens, {"start": offendingSymbol.tokenIndex+1, "end": 3})) &&
                offendingSymbol.text === ")")
                return 'Maybe your are missing the right-hand expression in a condition\n' +
                    'Here how to use a condition :\n (expression1 == expression2)\n (expression1 != expression2)';

            // RULE 4.2 (Accuracy 20%) : Missing a left-hand expression in a comparison of an IF_THEN condition
            if(findToken("(", tokens, {"start": offendingSymbol.tokenIndex+1, "end": 5}) &&
                (offendingSymbol.text === "==" || offendingSymbol.text === "!="))
                return 'Maybe your are missing a left-hand expression in a condition\n' +
                    'Here how to use a condition :\n (expression1 == expression2)\n (expression1 != expression2)';

             // RULE 4.3 (Accuracy ??%) : Missing parenthesis in a IF_THEN
            if(findToken("THEN", tokens, {"start": offendingSymbol.tokenIndex+1, "end": 3}))
                return 'Maybe your are missing a parenthesis in a IF_THEN condition\n' +
                    'Here how to use an IF_THEN : IF ( condition ) THEN { expression }';

            // RULE 4.4 (Accuracy ??%) : Missing parenthesis in a clause
            if(findToken("CLAUSE", tokens, {"start": offendingSymbol.tokenIndex+1, "end": 3}))
                return 'Maybe your are missing a parenthesis in a CLAUSE \n' +
                    'Here how declare a clause :\nCLAUSE clause_name ( expr )';

            // RULE 4.5 (Accuracy 10%) : Possibly missing = in a comparison of an IF_THEN condition
            if(findToken("THEN", tokens, {"start": offendingSymbol.tokenIndex+5, "end": 3}) ||
               findToken("IF", tokens, {"start": offendingSymbol.tokenIndex+1, "end": 10}))
                return 'Maybe your are missing an operator = or ! \n' +
                    'Here how to use comparison : (expr == expr) // (expr != expr)';

            break;
    }

    return res;
};



/***************************************
 *  Semantic linter
 ***************************************/
var walk = function(node, options) {
    var res = [];
    if(!options) options = {};
    if(!options.filter_type) options.filter_type = null;
    if(!options.filters) options.filters = null;
    if(!options.depth) options.depth = -1;

    if(options.depth == 0)
        return res;

    for(var child in node.children) {
        if(node.children.hasOwnProperty(child))
            res = res.concat(walk(node.children[child], options));
    }

    if(options.filter_type == null) {
        if(options.filters != null)
            if(eval(filters))
                res.push(node);
        else
            res.push(node);

    } else if(node instanceof options.filter_type) {
        if(options.filters != null) {
            if(eval(filters))
                res.push(node);
        }
        else
            res.push(node);
    }
    return res;
};

var getTokenName = function(token) {
    var res = token;
    if(token != undefined && token != null) {
        if((token instanceof Array) && token.length > 0) {
            if(token[0].hasOwnProperty("children"))
                res = token[0].children[0].symbol.text;
        }
        else if(token.hasOwnProperty("children")) {
            res = token.children[0].symbol.text;
        } else if (token.hasOwnProperty("symbol")) {
            res = token.symbol.text;
        }
    }
    return res;
};

function replaceAll(find, replace, str) {
  return str.replace(new RegExp(find, 'g'), replace);
}

var aalStdLib = ["core.macros", "core.types", "core.eu", "core.resolve", "core.sat", "core.validate"];
var aalStdLib_types = [];
var aalStdLib_services = [];
var aalStdLib_agents = [];
var aalStdLib_macros = [];


var hint_linter = function(tree) {
    var annotations = [];
    var line = 0, column = 0, msg = "", msgType = "info";
    var aat = analyseAALtree(tree);
    var loadedUserLibs = aat.libsNames.slice();
    for(var lib in aalStdLib) {
        var tmp = loadedUserLibs.indexOf(aalStdLib[lib]);
        if(tmp != -1)
            loadedUserLibs.splice(tmp, 1);
    }
    /**
     * RULE 1 : Checking that all used services are declared
     * Level : info | warning
     */
    for(var k in aat.actions) {
        if(aat.actions.hasOwnProperty(k)) {
            var serviceName = getTokenName(walk(aat.actions[k], {"filter_type": aal.AALParser.H_serviceIdContext}));
            if (aat.servicesNames.indexOf(serviceName) === -1) {
                line = aat.actions[k].start.line - 1;
                column = aat.actions[k].start.column;
                msg = "- " + serviceName + ((loadedUserLibs.length === 0)?" service is not declared !":
                        " service may be not declared !\n  Hint : you should compile the file in order to perform a backend check.");
                msgType = (loadedUserLibs.length > 0)?"info": "warning";

                annotations.push({row: line, column: column, text: msg, type: msgType});
            }
        }
    }

    /**
     * RULE 2 : Checking that all agents are declared
     * Level : info | warning
     */
    for(var k in aat.actions) {
        if(aat.actions.hasOwnProperty(k)) {
            var agentName = getTokenName(walk(aat.actions[k], {"filter_type": aal.AALParser.H_agentIdContext}));
            if (aat.agentsNames.indexOf(agentName) === -1) {
                line = aat.actions[k].start.line - 1;
                column = aat.actions[k].start.column;
                msg = "- " + agentName + ((loadedUserLibs.length === 0)?" agent is not declared !":
                        " agent may be not declared !\n  Hint : you should compile the file in order to perform a backend check.");
                msgType = (loadedUserLibs.length > 0)?"info": "warning";
                annotations.push({row: line, column: column, text: msg, type: msgType});
            }
        }
    }

    /**
     * RULE 3 : Checking types (basic)
     * Level : info
     */


    /**
     * RULE 4 : All clauses should have an auditing and rectification nodes
     * Level : info
     */

    /**
     * RULE 5 : Library core.types and should be loaded
     * Level : info
     */
    if(aat.libsNames.indexOf("core.types") === -1) {
        msg = '- You should probably load the library core.types\n  Use : LOAD "core.types"';
        annotations.push({row: 0, column: 0, text: msg, type: "info"});
    }

    /**
     * RULE 6 : Library core.macros and should be loaded
     * Level : info
     */
    if(aat.libsNames.indexOf("core.macros") === aat.libsNames.indexOf("core.sat") === aat.libsNames.indexOf("core.validate") === -1) {
        msg = '- You should probably load the macros library, it is required to perform  ' +
            '\n  to do so use : LOAD "core.macros"';
        annotations.push({row: 0, column: 0, text: msg, type: "info"});
    }


    /**
     * RULE 7 : Unused declarations
     * Level : warning
     */


    /**
     * RULE 8 : At least a PERMIT/DENY on each service
     * Level : info
     */


    /**
     * RULE 9 : Clause naming convention (actorName_???)
     * A clause is generally attached to an actor, thus the clause name should
     * contains the actor name.
     * Level : info
     */


    //annotations.push({row: line, column: column, text: msg, type: msgType});
    return annotations;
};


/*****************************************
 * Validation function
 * @param input
 * @returns {*}
 ****************************************/
var validate = function(input) {
    var stream = new antlr4.InputStream(input);
    var lexer = new aal.AALLexer(stream);
    var tokens = new antlr4.CommonTokenStream(lexer);
    var parser = new aal.AALParser(tokens);
    var annotations = [];
    var listener = new AnnotatingErrorListener(annotations);
    parser.removeErrorListeners();
    parser.addErrorListener(listener);
    var tree = parser.main();

    // If there is parsing errors, return the first one
    if(annotations.length > 0)
        return [annotations[0]];
    else
        // Apply linter rules
        return hint_linter(tree);
};

/**
 * Analyse AAL tree
 * @param tree
 * @returns {{actions, agents, agentsNames: *, services, servicesNames: *, types, clauses, clausesNames: *, libs, libsNames: *}}
 */
var analyseAALtree = function(tree) {
    var actions = walk(tree, {"filter_type": aal.AALParser.ActionContext});
    var agents = walk(tree, {"filter_type": aal.AALParser.AgentDecContext});
    var agentsNames = agents.map(function(v,i,a){ return getTokenName(walk(v, {"filter_type": aal.AALParser.H_agentIdContext})); });
    var services = walk(tree, {"filter_type": aal.AALParser.ServiceDecContext});
    var servicesNames = services.map(function(v,i,a){ return getTokenName(walk(v, {"filter_type": aal.AALParser.H_serviceIdContext})); });
    var types = walk(tree, {"filter_type": aal.AALParser.TypeDecContext});
    var clauses = walk(tree, {"filter_type": aal.AALParser.ClauseContext});
    var clausesNames = clauses.map(function(v,i,a){ return getTokenName(walk(v, {"filter_type": aal.AALParser.H_clauseIdContext})); });
    var libs = walk(tree, {"filter_type": aal.AALParser.LoadlibContext});
    var libsNames = libs.map(function(v,i,a){ var l = getTokenName(v.children[1]); return l.substring(1, l.length -1);});

    return {"actions": actions,
            "agents": agents, "agentsNames": agentsNames,
            "services": services, "servicesNames" : servicesNames,
            "types": types,
            "clauses": clauses, "clausesNames": clausesNames,
            "libs": libs, "libsNames": libsNames
    }
};

/**
 * Return the parsed AAL tree
 * @param input
 */
var parseAAL = function(input) {
    var stream = new antlr4.InputStream(input);
    var lexer = new aal.AALLexer(stream);
    var tokens = new antlr4.CommonTokenStream(lexer);
    var parser = new aal.AALParser(tokens);
    return parser.main();
};

/**
 * Worker
 */
ace.define('ace/worker/aal_worker',["require","exports","module","ace/lib/oop","ace/worker/mirror"], function(require, exports, module) {
    "use strict";

    var oop = require("ace/lib/oop");
    var Mirror = require("ace/worker/mirror").Mirror;

    var AALWorker = function(sender) {
        Mirror.call(this, sender);
        this.setTimeout(200);
        this.$dialect = null;
    };

    oop.inherits(AALWorker, Mirror);

    (function() {

        this.onUpdate = function() {
            var value = this.doc.getValue();
            var annotations = validate(value);
            this.sender.emit("annotate", annotations);
        };

        // Custom worker commands
        this.analyseAALtree = function(e) {
            var res = analyseAALtree(parseAAL(this.doc.getValue()));
            res = {"agents": res.agentsNames, "services" : res.servicesNames, "types": res.types,
                        "clauses": res.clausesNames, "libs": res.libsNames};
            this.sender.emit("callback", { "cmd": "analyseAALtree", "result": res});
        };

        this.getAgents = function(e) {
            var res = analyseAALtree(parseAAL(this.doc.getValue()));
            this.sender.emit("callback", {"cmd": "getAgents", "result": {"agents": res.agentsNames}});
        };

        this.getServices = function(e) {
            var res = analyseAALtree(parseAAL(this.doc.getValue()));
            this.sender.emit("callback", {"cmd": "getServices", "result": {"services": res.servicesNames}});
        };

        this.getClauses = function(e) {
            var res = analyseAALtree(parseAAL(this.doc.getValue()));
            this.sender.emit("callback", {"cmd": "getClauses", "result": {"clauses": res.clausesNames}});
        };

        this.analyseAALtreeForAcd = function(e) {
            var res = analyseAALtree(parseAAL(this.doc.getValue()));
            var agents = [];
            for(var i= 0; i<res.agents.length; i++) {
                var rs = walk(walk(res.agents[i],{"filter_type": aal.AALParser.RsServiceContext})[0],
                    {"filter_type": aal.AALParser.H_serviceIdContext});
                var rsNames = rs.map(function(v,i,a){ return getTokenName(v); });

                var ps = walk(walk(res.agents[i],{"filter_type": aal.AALParser.PsServiceContext})[0],
                    {"filter_type": aal.AALParser.H_serviceIdContext});
                var psNames = ps.map(function(v,i,a){ return getTokenName(v); });

                agents.push({name: getTokenName(res.agents[i].children[1]), types:[], ps:psNames, rs: rsNames})
            }
            res = {"agents": agents, "services" : res.servicesNames, "types": res.types,
                        "clauses": res.clausesNames, "libs": res.libsNames};
            this.sender.emit("callback", { "cmd": "analyseAALtreeForAcd", "result": res});
        };



    }).call(AALWorker.prototype);

    exports.MyWorker = AALWorker;
});
