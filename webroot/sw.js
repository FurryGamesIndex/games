const CACHE_NAME = "sw:i:1"

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
		if (!url.pathname.startsWith("/assets/") &&
		    !url.pathname.startsWith("/styles/") &&
		    !url.pathname.startsWith("/webfonts/"))
			return fetch(e.request.clone());

		const cache = await caches.open(CACHE_NAME);
		let resp = await cache.match(e.request);
		if (!resp) {
			resp = await fetch(e.request.clone());
			if (resp.status < 400) {
				console.log('sw: caching the response to', e.request.url);
				await cache.put(e.request, resp.clone());
			}
		}
		return resp;
	})());
});
