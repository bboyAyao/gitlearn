App({
    globalData: {
        g_isPlayingMusic: false, //解决播放音乐后重新进入当前文章页面，播放按钮自动变成未播放显示的bug
        g_currentMusicPostId: null, //解决播放音乐过程中进入其他文章，图片自动切换的bug
        doubanBase:"https://douban.uieee.com"
    }
})