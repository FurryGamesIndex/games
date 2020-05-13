window.$ = (selector => document.querySelector(selector));
Element.prototype.html = (html => this.innerHTML = html);
Element.prototype.text = (text => this.textContent = text);
Element.prototype.attr = (key => this.getAttribute(key));

