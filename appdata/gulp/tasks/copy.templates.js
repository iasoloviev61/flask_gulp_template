'use strict';
module.exports = function() {
  $.gulp.task('copy:templates', function() {
    return $.gulp.src('./source/template/**/*.*')
      .pipe($.gulp.dest($.config.root + '/template/'))
      .pipe($.browserSync.stream());
  });
};
