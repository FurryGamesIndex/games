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

window.add_infobar = (id, content) => {
	if (localStorage.getItem("current_hide_id") === id)
		return;

	const div = $('#infobar_rt ._content');
	if (div != null) {
		const element = $('#infobar_rt');
		div.innerHTML = content;
		element.classList.remove('hide');
		$('#infobar_rt ._cbtn').onclick = ((f, a, b) => event => f(a, b))((id, element) => {
			event.preventDefault();
			element.classList.add('hide');
			localStorage.setItem("current_hide_id", id);
		}, id, element);
	}
}

let stagingLangMap = {'ja': 'Japanese'}
let langs = ""
for (const lang in stagingLangMap) {
	if (navigator.languages.indexOf(lang) >= 0) {
		langs += stagingLangMap[lang] + ", ";
	}

	langs = langs.slice(0, -2);

	if (langs.length > 0) {
		add_infobar('want-translator',
			"Based on the language of your browser, it seems you know " +
			langs + ". Would you like to help us translate the " + langs +
			" version of the site? The maintainer can be contacted via " +
			"<a href='https://github.com/FurryGamesIndex/games'>Github</a>, " +
			"<a href='mailto:webmaster@furrygames.top'>Email</a> " +
			"or <a href='https://t.me/UtopicPanther'>Telegram</a>.");
	}
}

} catch (e) {
	console.log("FGI base.js load failed")
}
