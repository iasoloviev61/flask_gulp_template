'use strict';

module.exports = function() {
  $.gulp.task('serve', function() {
    $.browserSync.init({
        proxy: "172.17.0.1:5000",
        open: false,
        reloadDelay: 300,
        reloadDebounce: 500
    });

    $.browserSync.watch([$.config.root + '/**/*.*', '!**/*.css'], $.browserSync.reload);
  });
};
