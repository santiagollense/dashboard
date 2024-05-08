// service-worker.js

// Nombre de la caché
const CACHE_NAME = 'dashboard-cache-v1';

// Archivos a ser cacheados
const urlsToCache = [
  '/static/css/styles.css',
  '/static/js/main.js',
  '/api/actualizar_datos/',
];

// Instalación del Service Worker
self.addEventListener('install', event => {
  // Realizar la instalación
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

// Activación del Service Worker
self.addEventListener('activate', event => {
  // Borrar cachés antiguas
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.filter(cacheName => {
          return cacheName !== CACHE_NAME;
        }).map(cacheName => {
          return caches.delete(cacheName);
        })
      );
    })
  );
});

// Fetch
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // Si se encuentra en caché, devolver la respuesta en caché
        if (response) {
          return response;
        }

        // Si no está en caché, realizar la solicitud a la red
        return fetch(event.request)
          .then(response => {
            // Si la respuesta es válida, agregarla a la caché y devolverla
            if (!response || response.status !== 200 || response.type !== 'basic') {
              return response;
            }

            const responseToCache = response.clone();

            caches.open(CACHE_NAME)
              .then(cache => {
                cache.put(event.request, responseToCache);
              });

            return response;
          });
      })
  );
});
