const CACHE_NAME = "sw:i:7"

self.addEventListener('activate', async e => {
	e.waitUntil((async () => {
		const keys = await caches.keys();
		keys.forEach(async i => {
			if (i.startsWith("sw:") && i !== CACHE_NAME)
				await caches.delete(i);
		});
	})());
});

self.addEventListener('fetch', async e => {
	e.respondWith((async () => {
		const url = new URL(e.request.url);
		let nohint = true,
			uquery = false,
			cors = false,
			name = e.request;

		if (URL.prototype.hasOwnProperty("searchParams")) {
			hc = url.searchParams.get("hc");
			if (hc != null) {
				nohint = false;
				switch (hc) {
				case "uquery":
					uquery = true;
					break;
				}
				if (url.searchParams.get("cors")) {
					cors = true;
				}
			}
			const uid = url.searchParams.get("uid");
			if (uid != null) {
				url.searchParams.delete("uid");
				name = "/_virtual/" + uid + url.search;
			}
		}

		if (nohint &&
		    !url.pathname.startsWith("/assets/") &&
		    !url.pathname.startsWith("/styles/") &&
		    !url.pathname.startsWith("/webfonts/"))
			return fetch(e.request.clone());

		if (url.hostname !== self.location.hostname && !cors) {
			cors = true;
			console.warn("sw: cross-domain request should use CORS. Opaque cache avoided. URI:", e.request.url);
		}

		const cache = await caches.open(CACHE_NAME);
		let resp = await cache.match(name);
		if (!resp) {
			if (uquery) {
				const oldresp = await cache.matchAll(name, {
					"ignoreSearch": true
				});
				if (oldresp != null) {
					oldresp.forEach((el, index, arr) => {
						console.log('sw: deleting the response to', el.url);
						cache.delete(el.url);
					});
				}
			}
			let req;
			if (cors) {
				req = new Request(e.request.url, {mode: 'cors'});
			} else {
				req = e.request.clone();
			}
			resp = await fetch(req);
			if (resp.status < 400) {
				console.log('sw: caching the response to', e.request.url);
				await cache.put(name, resp.clone());
			}
		}
		return resp;
	})());
});
