var gulp = require('gulp'),
autoprefixer = require('gulp-autoprefixer'),
sass = require('gulp-sass'),
bulkSass = require('gulp-sass-bulk-import'),
sourcemaps = require('gulp-sourcemaps'),
browserSync = require('browser-sync').create(),
exec = require('child_process').exec,
fontgen = require('gulp-fontgen'),
reload = browserSync.reload;

const paths = {
    app:  './',
    css: '../dist/css',
	sass: './styles',
	templates: '../templates'
}

gulp.task('styles', function() {
	console.log(paths.sass);
	gulp.src(paths.sass + '/styles.scss')
	.pipe(sourcemaps.init())
	.pipe(bulkSass())
	.pipe(sass().on('error', onError))
	.pipe(autoprefixer({browsers: ['last 2 version']}))
	.pipe(sourcemaps.write())
	.pipe(gulp.dest(paths.css));
});


gulp.task('runserver', function() {
	exec('HOST_PORT=3000 python ../server/manage.py runserver', function (err, stdout, stderr) {
		console.log(stdout);
		console.log(stderr);
	});
})

gulp.task('browserSyncTask', ['runserver'], function() {
	browserSync.init({
		notify: false,
		proxy: 'localhost:8000'
	});
});

gulp.task('watchTask', function() {
	gulp.watch(paths.sass + '/**/*.scss', ['styles', reload]);
	gulp.watch(paths.sass + '/**/**/*.scss', ['styles', reload]);
	gulp.watch([paths.templates + '/*.html',
				paths.templates + '/**/*.html',
				paths.templates + '/**/**/*.html'], reload);	
});

gulp.task('default', ['styles', 'watchTask', 'browserSyncTask']);

gulp.task('prod_css', function() {
	gulp.src(paths.sass + '/styles.scss')
		.pipe(bulkSass())
		.pipe(sass({outputStyle: 'compressed'}).on('error', onError))
		.pipe(autoprefixer({browsers: ['last 2 version']}))
		.pipe(gulp.dest(paths.css));
});

gulp.task('build', ['prod_css',]);