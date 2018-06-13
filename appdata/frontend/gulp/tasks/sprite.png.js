'use strict';
module.exports = function () {
  $.gulp.task('sprite:png', function () {
    var spriteData = $.gulp.src('./source/sprite/png/*.png')
        .pipe($.spritesmith({
          imgName: 'sprite.png',
          cssName: '_spritepng.scss',
          algorithm: 'binary-tree'
        }));
    var imgStream = spriteData.img
       .pipe($.gulp.dest($.config.root + '/assets/img'));
    var cssStream = spriteData.css
        .pipe($.gulp.dest('./source/style/_blocks'));
    return $.merge(imgStream, cssStream);
  })
};