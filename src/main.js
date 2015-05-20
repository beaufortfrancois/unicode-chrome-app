
var xhr = new XMLHttpRequest();
xhr.open('GET', chrome.runtime.getURL('UnicodeData.txt'));
xhr.onload = function() {
  var data = xhr.response.split('\n');
  var textContent = '';
  for (var line of data) {
    if (!line.length)
      continue
    textContent = String.fromCodePoint(parseInt(line.split(';')[0], 16)) + ' ' + textContent;
  }
  document.body.textContent = textContent;
};
xhr.send();