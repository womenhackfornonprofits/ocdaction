module.exports = function(grunt) {
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-copy');

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    //------- CSS Minify -------//
    cssmin: {
      combine: {
        files: {
          '../ocdaction/static/styles/styles.css': ['css/styles.css']
        }
      }
    },

    //------- SASS -------//
    sass: {
      dist: {
        files: {
          'css/styles.css': 'src/sass/styles.scss'
        }
      }
    },

    //------- Watch SASS -> CSS -------//
    watch: {
      sass: {
        files: 'src/sass/**/**.scss',
        tasks: ['sass', 'cssmin']
      }
    },

    jspaths: {
      src: {
        js: 'src/**/**.js'
      },
      dest: {
        jsMin: '../ocdaction/static/scripts/ocdaction.min.js'
      }
    },

    //------- JS Minify ------//
    uglify: {
      options: {
        compress: true,
        mangle: true,
        sourceMap: true
      },
      target: {
        src: '<%= jspaths.src.js %>',
        dest: '<%= jspaths.dest.jsMin %>'
      }
    },

    //------- copy remaining static files ------//
    copy: {
      img: {
        files: [{
          expand: true,
          nonull: true,
          cwd: 'src/img',
          src: ['*.{png,jpg,jpeg,svg,gif}'],
          dest: '../ocdaction/static/img/',
          filter: 'isFile'
        }]
      }
    }

  });

  grunt.registerTask('default', ['sass', 'cssmin', 'uglify', 'copy']);

};
