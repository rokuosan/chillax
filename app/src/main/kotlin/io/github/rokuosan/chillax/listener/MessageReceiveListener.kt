package io.github.rokuosan.chillax.listener

import com.sedmelluq.discord.lavaplayer.player.AudioLoadResultHandler
import com.sedmelluq.discord.lavaplayer.player.DefaultAudioPlayerManager
import com.sedmelluq.discord.lavaplayer.source.AudioSourceManagers
import com.sedmelluq.discord.lavaplayer.source.youtube.YoutubeAudioSourceManager
import com.sedmelluq.discord.lavaplayer.tools.FriendlyException
import com.sedmelluq.discord.lavaplayer.track.AudioPlaylist
import com.sedmelluq.discord.lavaplayer.track.AudioTrack
import io.github.rokuosan.chillax.GuildTrackManagers
import io.github.rokuosan.chillax.handler.EchoHandler
import io.github.rokuosan.chillax.manager.GuildTrackManager
import net.dv8tion.jda.api.events.GenericEvent
import net.dv8tion.jda.api.events.message.MessageReceivedEvent
import net.dv8tion.jda.api.hooks.EventListener


class MessageReceiveListener: EventListener {
    override fun onEvent(e: GenericEvent) {
        if (e !is MessageReceivedEvent) return
        if (e.author.isBot) return
        if (!e.isFromGuild) return

        val apm = DefaultAudioPlayerManager()
        AudioSourceManagers.registerRemoteSources(apm);
        AudioSourceManagers.registerLocalSource(apm);

        val cmd = e.message.contentRaw.split(" ")
        when(cmd[0].lowercase()) {
            "!join" -> {
                val m = e.member?:return
                val vs = m.voiceState
                val ch = vs?.channel?:return

                val guild = ch.guild
                val am = guild.audioManager
                val handler = EchoHandler()

                am.sendingHandler = handler
                am.receivingHandler = handler
                am.openAudioConnection(ch)
            }
            "!quit" -> {
                val m = e.member?:return
                val vs = m.voiceState
                val ch = vs?.channel?:return

                val guild = ch.guild
                val am = guild.audioManager

                am.closeAudioConnection()
            }
            "~play" -> {
                val gtm = GuildTrackManagers[e.guild.idLong]?:run {
                    val gtm = GuildTrackManager(apm)
                    GuildTrackManagers[e.guild.idLong] = gtm
                    gtm
                }
                val ch = e.channel

                apm.loadItemOrdered(gtm, cmd[1], object: AudioLoadResultHandler {
                    override fun trackLoaded(track: AudioTrack?) {
                        if (track == null) return
                        ch.sendMessage("Loaded ${track.info?.title}").queue()

                        val c = e.member?.voiceState?.channel?:return
                        val am = e.guild.audioManager
                        if (!am.isConnected) {
                            am.openAudioConnection(c)
                        }

                        gtm.scheduler.queue(track)
                    }

                    override fun playlistLoaded(p0: AudioPlaylist?) {
                        TODO("Not yet implemented")
                    }

                    override fun noMatches() {
                        ch.sendMessage("No matches").queue()
                    }

                    override fun loadFailed(p0: FriendlyException?) {
                        ch.sendMessage("Load failed").queue()
                    }
                })
            }
        }
    }
}
