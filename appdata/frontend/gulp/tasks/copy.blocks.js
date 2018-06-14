'use strict';
module.exports = function() {
  $.gulp.task('copy:blocks', function() {
    return $.gulp.src('./source/blocks/**/*.pug')
      .pipe($.gulp.dest($.config.root + '/template/blocks/'))
      .pipe($.browserSync.stream());
  });
};
