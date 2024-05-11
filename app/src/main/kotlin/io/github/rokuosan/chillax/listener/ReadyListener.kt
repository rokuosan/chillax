package io.github.rokuosan.chillax.listener

import net.dv8tion.jda.api.events.GenericEvent
import net.dv8tion.jda.api.events.session.ReadyEvent
import net.dv8tion.jda.api.hooks.EventListener

class ReadyListener: EventListener {
    override fun onEvent(e: GenericEvent) {
        if (e !is ReadyEvent) return

        println("API is ready!")
    }
}
