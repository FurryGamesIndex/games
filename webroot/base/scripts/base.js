try {
window.$ = (selector => document.querySelector(selector));
window.$$ = (selector => document.querySelectorAll(selector));
String.prototype.format = function() {
	return this.replace(/{(\d+)}/g, (match, number) => {
		return typeof arguments[number] != 'undefined' ? arguments[number] : match;
	});
};

window.make_picture = (data, _prefix, picture) => {
	if (picture == null)
		picture = document.createElement("picture");

	data.source.forEach(i => {
		const prefix = (i.remote ? "" : _prefix);
		const source = document.createElement("source");
		source.setAttribute("type", i.type);
		source.setAttribute("srcset", prefix + i.srcset);
		picture.appendChild(source);
	});

	const srcnode = document.createElement("img");
	const prefix = (data.src_remote ? "" : _prefix);
	srcnode.src = prefix + data.src;
	picture.appendChild(srcnode);

	picture.srcNode = srcnode;
	return picture;
}

if ('serviceWorker' in navigator)
	navigator.serviceWorker.register('/sw.js');

} catch (e) {
	console.log("FGI base.js load failed")
}
