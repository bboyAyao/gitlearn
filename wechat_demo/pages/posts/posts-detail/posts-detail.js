var postsData = require('../../../data/posts-data.js')
var app = getApp()
Page({
    data: {
        isPlayingMusic: false
    },
    onLoad: function(options) {
        var postId = options.id
        this.data.postId = postId
        var postData = postsData.postList[postId];
        // console.log(postData.dateTime)?
        this.setData({
            postData: postData
        });

        var postsCollected = wx.getStorageSync('posts_collected')
        if (postsCollected) {
            var postCollected = postsCollected[postId]
            //将undefined转换为false，防止报错
            if (!postCollected) {
                postCollected = false
            }
            this.setData({
                collected: postCollected
            })
        } else {
            var postsCollected = {}
            postsCollected[postId] = false
            wx.setStorageSync('posts_collected', postsCollected)
        }

        if (app.globalData.g_isPlayingMusic && app.globalData.g_currentMusicPostId == postId) {
            this.setData({
                isPlayingMusic: true
            })
        }
        this.setAudioMonitor()
    },

    setAudioMonitor: function() {
        var that = this
        var bgAM = wx.getBackgroundAudioManager()
        bgAM.onPlay(function() {
            that.setData({
                isPlayingMusic: true
            })
            app.globalData.g_isPlayingMusic = true
            app.globalData.g_currentMusicPostId = that.data.postId
        })
        bgAM.onPause(function() {
            that.setData({
                isPlayingMusic: false
            })
            app.globalData.g_isPlayingMusic = false
            app.globalData.g_currentMusicPostId = null
            console.log('onpause...')
            console.log(that.data.isPlayingMusic)
        })
        bgAM.onStop(function() {
            that.setData({
                isPlayingMusic: false
            })
            app.globalData.g_isPlayingMusic = false
            app.globalData.g_currentMusicPostId = null
        })

    },
    // setAudioMonitor: function() {
    //     var that = this
    //     wx.onBackgroundAudioPlay(function() {
    //         that.setData({
    //             isPlayingMusic: true
    //         })
    //         app.globalData.g_isPlayingMusic = true
    //         app.globalData.g_currentMusicPostId = that.data.postId
    //     })
    //     wx.onBackgroundAudioPause(function() {
    //         that.setData({
    //             isPlayingMusic: false
    //         })
    //         app.globalData.g_isPlayingMusic = false
    //         app.globalData.g_currentMusicPostId = null
    //     })
    // },

    onCollectionTap: function(event) {
        this.getPostsColllectedSyc()
    },
    //同步获取缓存
    getPostsColllectedSyc: function() {
        var postsCollected = wx.getStorageSync('posts_collected')
        var postCollected = postsCollected[this.data.postId]
        postCollected = !postCollected
        postsCollected[this.data.postId] = postCollected
        //更新文章是否收藏的缓存值
        wx.setStorageSync('posts_collected', postsCollected)
        this.setData({
            collected: postCollected
        })
        // this.showModal(postsCollected, postCollected)
        wx.showToast({
            title: postCollected ? "收藏成功" : "取消成功",
            duration: 1000,
            icon: "success"
        })
    },
    // getPostsColllectedAsy:function(){
    //     var that = this
    //     //异步获取缓存
    //     wx.getStorage({
    //         key: 'posts_collected',
    //         success: function(res) {
    //             var postsCollected = res.data;
    //             var postCollected = postsCollected[that.data.postId]
    //             postCollected = !postCollected
    //             postsCollected[that.data.postId] = postCollected
    //             //更新文章是否收藏的缓存值
    //             wx.setStorage({
    //                 key: 'posts_collected',
    //                 data: postsCollected,
    //             })
    //             that.setData({
    //                 collected: postCollected
    //             })
    //             wx.showToast({
    //                 title: postCollected ? "收藏成功" : "取消成功",
    //                 duration: 1000,
    //                 icon: "success"
    //             })
    //         },
    //     })
    // },

    onMusicTap: function() {
        var postId = this.data.postId
        var postData = postsData.postList[postId]
        var isPlayingMusic = this.data.isPlayingMusic
        var bgAM = wx.getBackgroundAudioManager()
        if (isPlayingMusic) {
            bgAM.pause()
            this.setData({
                isPlayingMusic: false
            })
        } else {
            bgAM.src = postData.music.url
            bgAM.title = postData.music.title
            bgAM.coverImgUrl = postData.music.coverImg
            // var rel = bgAM.play()

            this.setData({
                isPlayingMusic: true
            })
        }

        // var postId = this.data.postId
        // var postData = postsData.postList[postId]
        // var isPlayingMusic = this.data.isPlayingMusic
        // if(isPlayingMusic){
        //     wx.pauseBackgroundAudio();
        //     this.setData({
        //         isPlayingMusic:false
        //     })
        // }
        // else{
        //     wx.playBackgroundAudio({
        //         dataUrl: postData.music.url,
        //         title: postData.music.title,
        //         coverImgUrl: postData.music.coverImg
        //     })
        //     this.setData({
        //         isPlayingMusic: true
        //     })
        // }

    },
    onShareTap: function(event) {
        wx.getSystemInfo({
            success: function(result) {
                console.log(result.platform)
                //选项集合
                var itemList;
                if (result.platform == 'android') {
                    itemList = [
                        "分享到微信好友",
                        "分享到朋友圈",
                        "分享到QQ",
                        "分享到微博",
                        "取消",
                    ]
                } else {
                    itemList = [
                        "分享到微信好友",
                        "分享到朋友圈",
                        "分享到QQ",
                        "分享到微博",
                    ]
                }
                wx.showActionSheet({
                    itemList: itemList,
                    itemColor: "#405f80",
                    success: function(res) {
                        if (res.tapIndex != 4) {
                            wx.showModal({
                                title: "分享成功",
                                content: "已成功" + itemList[res.tapIndex],
                            })
                        }
                    }
                })
            }
        })
    }
    // showModal: function(postsCollected, postCollected) {
    //     var that = this
    //     wx.showModal({
    //         title: "收藏",
    //         content: postCollected?"收藏该文章":"取消收藏该文章",
    //         showCancel: true,
    //         cancelText:"取消",
    //         cancelColor:"#333",
    //         confirmText: "确认",
    //         confirmColor: "#405f80",
    //         success:function(res){
    //             if(res.confirm){
    //                 wx.setStorageSync('posts_collected', postsCollected)
    //                 that.setData({
    //                     collected:postCollected 
    //                 })
    //             }
    //         }
    //     })
    // }
})