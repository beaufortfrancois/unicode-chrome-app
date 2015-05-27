/**
 * Listens for the app launching, then creates the window.
 *
 * @see http://developer.chrome.com/apps/app.runtime.html
 * @see http://developer.chrome.com/apps/app.window.html
 */
chrome.app.runtime.onLaunched.addListener(function(launchData) {
  chrome.app.window.create(
    'index.html',
    {
      id: 'id',
      hidden: true,
      frame: {color: '#455A64'},
      innerBounds: {minWidth: 360, width: 360, minHeight: 640, height: 640}
    }
  );
});
