var postsData = require('../../data/posts-data.js')

Page({
    data: {
    },
    onLoad: function() {
        
        this.setData({
            posts_key: postsData.postList
            })
    },
    onPostTap:function(event){
        var postId = event.currentTarget.dataset.postId
        // console.log(postId)
        wx.navigateTo({
            url: 'posts-detail/posts-detail?id='+postId,
        })
    },
    onSwiperTap:function(event){
        var postId = event.target.dataset.postId
        console.log(postId)
        wx.navigateTo({
            url: 'posts-detail/posts-detail?id=' + postId,
        })
    }
})