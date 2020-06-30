const gulp = require('gulp');
const htmlmin = require('gulp-htmlmin');
const imagemin = require('gulp-imagemin');
const cleanCSS = require('gulp-clean-css');
const concat = require('gulp-concat');
const uglify = require('gulp-uglify');
const pipeline = require('readable-stream').pipeline;

let djangoBlockCondition=/{%(.*?)%}/;
let djangoVariableCondition=/{{(.*?)}}/;
let ampImgCondition=/<amp-img([\s\S]*?)amp-img>/;
let ampCarouselCondition=/<amp-carousel([\s\S]*?)amp-carousel>/;
let sum_condition = [djangoBlockCondition,djangoVariableCondition,ampImgCondition,ampCarouselCondition]

// TASKS: *** MINIFY HTML ***

gulp.task('minifyAnalysisHtml',function() {
    return gulp.src('analysis/templates/analysis/dev/*.html')
        .pipe(htmlmin({collapseWhitespace: true, ignoreCustomFragments:sum_condition }))
        .pipe(gulp.dest('analysis/templates/analysis/prod/'));
});

gulp.task('minifyContactsHtml', function() {
    return gulp.src('contacts/templates/contacts/dev/*.html')
        .pipe(htmlmin({collapseWhitespace: true, ignoreCustomFragments:sum_condition }))
        .pipe(gulp.dest('contacts/templates/contacts/prod/'));
});

gulp.task('minifyArticlesNewsHtml', function() {
    return gulp.src('articles/templates/articles/dev/*.html')
        .pipe(htmlmin({collapseWhitespace: true, ignoreCustomFragments:sum_condition }))
        .pipe(gulp.dest('articles/templates/articles/prod/'));
});

gulp.task('minifyPositionHtml', function() {
    return gulp.src('positions/templates/positions/dev/*.html')
        .pipe(htmlmin({collapseWhitespace: true, ignoreCustomFragments:sum_condition }))
        .pipe(gulp.dest('positions/templates/positions/prod/'));
});

gulp.task('minifyPricelistHtml', function() {
    return gulp.src('pricelist/templates/pricelist/dev/*.html')
        .pipe(htmlmin({collapseWhitespace: true, ignoreCustomFragments: sum_condition}))
        .pipe(gulp.dest('pricelist/templates/pricelist/prod/'));
});


gulp.task('minifyCoreHtml', function() {
    return gulp.src('core/templates/core/dev/*.html')
        .pipe(htmlmin({collapseWhitespace: true, ignoreCustomFragments:sum_condition }))
        .pipe(gulp.dest('core/templates/core/prod/'));
});

gulp.task('minifyWikiHtml', function() {
    return gulp.src('wiki/templates/wiki/dev/*.html')
        .pipe(htmlmin({collapseWhitespace: true, ignoreCustomFragments:sum_condition }))
        .pipe(gulp.dest('wiki/templates/wiki/prod/'));
});

// TASKS: *** CONCAT AND COMPRESS CSS ***

gulp.task('createProdCss', function() {
  return gulp.src(['core/static/core/css/dev/base.css', 'core/static/core/css/dev/576.css',
      'core/static/core/css/dev/768.css', 'core/static/core/css/dev/992.css', 'core/static/core/css/dev/custom.css'])
    .pipe(concat('prod.css'))
    .pipe(cleanCSS({compatibility: 'ie8'}))
    .pipe(gulp.dest('core/static/core/css/prod/'));
});

gulp.task('minifyContactsCss', () => {
  return gulp.src('contacts/static/contacts/css/dev/*.css')
    .pipe(cleanCSS({compatibility: 'ie8'}))
    .pipe(gulp.dest('contacts/static/contacts/css/prod/'));
});

// TASKS: *** CONCAT AND COMPRESS JS ***

gulp.task('collectCoreJS', function() {
  return gulp.src(['core/static/core/vendor/smooth-scroll/smooth-scroll.polyfills.min.js', 'core/static/core/js/dev/navbar-dev.js'])
    .pipe(concat('core.js'))
    .pipe(gulp.dest('core/static/core/js/prod/'));
});

gulp.task('compressCoreJs', function () {
  return pipeline(
        gulp.src('core/static/core/js/prod/*.js'),
        uglify(),
        gulp.dest('core/static/core/js/prod/')
  );
});

gulp.task('collectPricelistJS', function() {
  return gulp.src(['pricelist/static/pricelist/vendor/tabs/tabby.min.js', 'pricelist/static/pricelist/vendor/tabs/tabby.polyfills.min.js',
  'core/static/core/vendor/lightgallery/lightgallery.min.js'])
    .pipe(concat('pricelist.js'))
    .pipe(gulp.dest('pricelist/static/pricelist/js/prod/'));
});

gulp.task('compressPricelistJS', function () {
  return pipeline(
        gulp.src('pricelist/static/pricelist/js/prod/*.js'),
        uglify(),
        gulp.dest('pricelist/static/pricelist/js/prod/')
  );
});


// TASKS: *** COMPRESS IMAGES ***

gulp.task('minifyImages', function() {
    return gulp.src('files/media/*')
        .pipe(imagemin())
        .pipe(gulp.dest('files/media/prod/'));
});

// *** COMBINE TASKS ***

gulp.task('prepareHtml', gulp.series('minifyAnalysisHtml', 'minifyContactsHtml',
    'minifyArticlesNewsHtml', 'minifyPositionHtml', 'minifyPricelistHtml', 'minifyCoreHtml', 'minifyWikiHtml'));

gulp.task('prepareCss', gulp.series('createProdCss', 'minifyContactsCss'));

gulp.task('prepareJS', gulp.series('collectCoreJS', 'compressCoreJs', 'collectPricelistJS', 'compressPricelistJS'));

