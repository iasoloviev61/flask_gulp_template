'use strict';
// переносим остальные файлы - favico и прочее
module.exports = function() {
  $.gulp.task('copy:files', function() {
    return $.gulp.src('./source/*.*', '!./source/*.html')
      .pipe($.gulp.dest($.config.root));
  });
};
