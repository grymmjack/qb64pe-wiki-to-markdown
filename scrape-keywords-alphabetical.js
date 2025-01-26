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
    sout_lang_keywords = keywords.filter(function(el) {
      return el.substring(0,1) != '$' && el.indexOf('(') == -1 && el.indexOf(')') == - 1 && el.indexOf('...') == -1;
    }).join('|');
    sout_lang_keywords_preprocessor = keywords.filter(function(el) {
      return el.substring(0,1) == '$' && el.indexOf('(') == -1 && el.indexOf(')') == - 1 && el.indexOf('...') == -1;
    }).join('|');
    sout_lang_keywords = sout_lang_keywords.replaceAll('$', '\\\\$');
        sout_lang_keywords_preprocessor = sout_lang_keywords_preprocessor.replaceAll('$', '\\\\$');
});
console.log(sout);
console.log(sout_lang_keywords);
console.log(sout_lang_keywords_preprocessor);
