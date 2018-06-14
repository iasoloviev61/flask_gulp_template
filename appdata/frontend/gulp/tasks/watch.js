'use strict';

module.exports = function() {
  $.gulp.task('watch', function() {
    $.gulp.watch('./source/js/**/*.js', $.gulp.series('js:process'));
    $.gulp.watch('./source/**/*.scss', $.gulp.series('sass'));
    $.gulp.watch('./source/template/**/*.pug', $.gulp.series('copy:templates'));
    $.gulp.watch('./source/blocks/**/*.pug', $.gulp.series('copy:templates'));
    $.gulp.watch('./source/images/**/*.*', $.gulp.series('copy:image'));
    $.gulp.watch($.path.jsFoundation, $.gulp.series('css:foundation'));
    $.gulp.watch($.path.jsFoundation, $.gulp.series('js:foundation'));
  });
};
