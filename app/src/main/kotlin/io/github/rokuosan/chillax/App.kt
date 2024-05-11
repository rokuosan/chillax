package io.github.rokuosan.chillax

import io.github.rokuosan.chillax.listener.ReadyListener
import net.dv8tion.jda.api.JDABuilder

fun main() {
    val token = System.getenv("DISCORD_TOKEN")?:run{
        println("DISCORD_TOKEN is not set")
        return
    }

    val jda = JDABuilder.createDefault(token)
        .addEventListeners(ReadyListener())
        .build()

    jda.awaitReady()
}
