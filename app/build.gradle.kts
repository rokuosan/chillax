plugins {
    alias(libs.plugins.jvm)
    application
}

repositories {
    mavenCentral()
    maven("https://jitpack.io")
}

dependencies {
    implementation(libs.jda)
    implementation(libs.logback)
    implementation(libs.lavaplayer)

    testImplementation("org.jetbrains.kotlin:kotlin-test-junit5")
    testImplementation(libs.junit.jupiter.engine)

    testRuntimeOnly("org.junit.platform:junit-platform-launcher")
    implementation(libs.guava)
}

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(21)
    }
}

application {
    mainClass = "io.github.rokuosan.chillax.AppKt"
}

tasks.named<Test>("test") {
    useJUnitPlatform()
}
