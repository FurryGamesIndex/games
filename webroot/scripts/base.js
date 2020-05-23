try {
window.$ = (selector => document.querySelector(selector));
window.$$ = (selector => document.querySelectorAll(selector));
String.prototype.format = function() {
	return this.replace(/{(\d+)}/g, (match, number) => {
		return typeof arguments[number] != 'undefined' ? arguments[number] : match;
	});
};
} catch (e) {
	console.log("FGI base.js load failed")
}
