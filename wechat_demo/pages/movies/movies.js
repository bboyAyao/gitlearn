// pages/movies/movies.js
var util = require('../../utils/util.js')
var app = getApp()
Page({
    data: {
        inTheaters: {},
        comingSoon: {},
        searchResult:{},
        top250: {},
        containerShow:true,
        searchPanelShow:false
    },
    onLoad: function(options) {
        var inTheatersUrl = app.globalData.doubanBase + "/v2/movie/in_theaters" + "?start=0&count=3"
        var coningSoonUrl = app.globalData.doubanBase + "/v2/movie/coming_soon" + "?start=0&count=3"
        var top250Url = app.globalData.doubanBase + "/v2/movie/top250" + "?start=0&count=3"

        util.http(inTheatersUrl, this.processDoubanData, "inTheaters", "正在热映")
        util.http(coningSoonUrl, this.processDoubanData, "coningSoon", "即将上映")
        util.http(top250Url, this.processDoubanData, "top250", "豆瓣Top250")
    },
    onMoreTap: function(event) {
        var category = event.currentTarget.dataset.category
        wx.navigateTo({
            url: 'more-movie/more-movie?category=' + category
        })
    },
    onMovieTap:function(event){
        var movieId = event.currentTarget.dataset.movieId
        wx.navigateTo({
            url: 'movie-detail/movie-detail?id=' + movieId
        })
    },
    onCancelImgTap:function(event){
        this.setData({
            containerShow:true,
            searchPanelShow:false,
            searchResult:{}
        })
    },  

    onBindFocus: function(event) {
        this.setData({
            containerShow:false,
            searchPanelShow:true
        })
    },
    onBindConfirm:function(event){
        var text =event.detail.value
        var searchUrl = app.globalData.doubanBase +'/v2/movie/search?q=' + text
        // var searchUrl = 'https://api.douban.com/v2/movie/search?q=' + text
        util.http(searchUrl, this.processDoubanData,'searchResult','')
        console.log(text)
    },

    processDoubanData: function(moviesDouban, settedKey, categoryTitle) {
        var movies = []
        for (var idx in moviesDouban.subjects) {
            var subject = moviesDouban.subjects[idx]
            var title = subject.title
            if (title.length >= 6) {
                title = title.substring(0, 6) + "..."
            }
            var temp = {
                stars: util.converToStarsArray(subject.rating.stars),
                title: title,
                average: subject.rating.average,
                coverageUrl: subject.images.large,
                movieId: subject.id
            }
            movies.push(temp)
        }
        var readyData = {};
        readyData[settedKey] = {
            categoryTitle: categoryTitle,
            movies: movies
        };
        this.setData(readyData)
    }
})