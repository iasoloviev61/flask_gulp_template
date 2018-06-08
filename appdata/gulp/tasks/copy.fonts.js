'use strict';
module.exports = function() {
  $.gulp.task('copy:fonts', function() {
    return $.gulp.src('./source/fonts/**/*.*')
      // .pipe($.filter(['*.eot', '*.svg', '*.ttf', '*.woff', '*.woff2']))
      .pipe($.gulp.dest($.config.root + '/assets/fonts'));
  });
};
