package io.github.rokuosan.chillax.manager

import com.sedmelluq.discord.lavaplayer.player.AudioPlayer
import com.sedmelluq.discord.lavaplayer.player.AudioPlayerManager
import io.github.rokuosan.chillax.handler.AudioPlayerSendHandler
import io.github.rokuosan.chillax.scheduler.TrackScheduler

class GuildTrackManager(
    manager: AudioPlayerManager
) {
    val player: AudioPlayer = manager.createPlayer()
    val scheduler: TrackScheduler = TrackScheduler(player).apply {
        player.addListener(this)
    }

    fun getSendHandler() = AudioPlayerSendHandler(this.player)
}
