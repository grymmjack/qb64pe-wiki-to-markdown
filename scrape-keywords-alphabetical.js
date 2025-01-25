console.clear();
keywords = [];
$('ul li a').each(function(i, el) { 
  	if (kw = el.href.split('/')[5]) {
      if (kw.indexOf(':') == -1) {
        switch(kw) {
            case '%26B': 
            	kw = '&B';
            case '%26H':
              kw = '&H';
            case '%26O':
              kw = '&O';
            case '%2B':
              kw = '-PLUS-';
            case '%5C':
              kw = '-BACKSLASH-';
            case '%5E':
              kw = '-CARET-';
            case '*':
              kw = '-ASTERISK-';
            case '-':
              kw = '-DASH-';
        }
        keywords.push(kw);
      }
    }
    keywords.sort();
  	keyset = new Set(keywords); 
  	keywords = Array.from(keyset); 
  	sout = keywords.join('\n'); 
}); 
console.log(sout);