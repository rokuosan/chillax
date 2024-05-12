package io.github.rokuosan.chillax.listener

import net.dv8tion.jda.api.events.GenericEvent
import net.dv8tion.jda.api.events.session.ReadyEvent
import net.dv8tion.jda.api.hooks.EventListener
import org.slf4j.LoggerFactory

class ReadyListener: EventListener {
    private val logger = LoggerFactory.getLogger(this::class.java)

    override fun onEvent(e: GenericEvent) {
        if (e !is ReadyEvent) return
        logger.info("Logged in as ${e.jda.selfUser.name}")

//        val pm = DefaultAudioPlayerManager()
//        AudioSourceManagers.registerRemoteSources(pm)
//        val p = pm.createPlayer()
//        val ts = TrackScheduler()
//
//        val guilds = e.jda.guilds
//        for (guild in guilds) {
//            guild.voiceChannels.forEach { vc ->
//                if (vc.name == "Chillax") {
//                    val am = guild.audioManager
//                    am.sendingHandler = AudioPlayerSendHandler(pm.createPlayer())
//                    am.openAudioConnection(vc)
//                }
//            }
//        }
    }
}
