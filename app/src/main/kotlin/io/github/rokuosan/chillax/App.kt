package io.github.rokuosan.chillax

import io.github.rokuosan.chillax.listener.MessageReceiveListener
import io.github.rokuosan.chillax.listener.ReadyListener
import io.github.rokuosan.chillax.manager.GuildTrackManager
import net.dv8tion.jda.api.JDABuilder
import net.dv8tion.jda.api.requests.GatewayIntent


val GuildTrackManagers = mutableMapOf<Long, GuildTrackManager>()

fun main() {
    val token = System.getenv("DISCORD_TOKEN")?:run{
        println("DISCORD_TOKEN is not set")
        return
    }

    val jda = JDABuilder.createDefault(token)
        .enableIntents(
            GatewayIntent.MESSAGE_CONTENT,
        )
        .addEventListeners(
            ReadyListener(),
            MessageReceiveListener(),
        ).build()

    jda.awaitReady()
}
