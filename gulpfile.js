const gulp = require('gulp');
const htmlmin = require('gulp-htmlmin');
const imagemin = require('gulp-imagemin');
const cleanCSS = require('gulp-clean-css');

// TASKS: *** MINIFY HTML ***

gulp.task('minifyContactsHtml', function() {
    return gulp.src('contacts/templates/contacts/dev/*.html')
        .pipe(htmlmin({collapseWhitespace: true }))
        .pipe(gulp.dest('contacts/templates/contacts/prod/'));
});

gulp.task('minifyArticlesNewsHtml', function() {
    return gulp.src('articles/templates/articles/dev/*.html')
        .pipe(htmlmin({collapseWhitespace: true }))
        .pipe(gulp.dest('articles/templates/articles/prod/'));
});

gulp.task('minifyPositionHtml', function() {
    return gulp.src('positions/templates/positions/dev/*.html')
        .pipe(htmlmin({collapseWhitespace: true }))
        .pipe(gulp.dest('positions/templates/positions/prod/'));
});

gulp.task('minifyWikiHtml', function() {
    return gulp.src('wiki/templates/wiki/dev/*.html')
        .pipe(htmlmin({collapseWhitespace: true }))
        .pipe(gulp.dest('wiki/templates/wiki/prod/'));
});

// TASKS: *** COMPRESS IMAGES ***

gulp.task('minifyImages', function() {
    return gulp.src('files/media/*')
        .pipe(imagemin())
        .pipe(gulp.dest('files/media/prod/'));
});

// TASKS: *** MINIFY CSS ***

gulp.task('minifyContactsCss', () => {
  return gulp.src('contacts/static/contacts/css/dev/*.css')
    .pipe(cleanCSS({compatibility: 'ie8'}))
    .pipe(gulp.dest('contacts/static/contacts/css/prod/'));
});

// *** COMBINE TASKS ***
