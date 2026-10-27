<script setup>
import { ref } from 'vue'

// Reactive state for the "Copied!" message when copying email
const copyStatus = ref('')

// Array of projects — adding a new project is as simple as adding a new object here!
const projects = [
  {
    title: 'MemTrack library',
    language: 'C / C++',
    description: 'A single header library in C/C++ that tracks memory allocations and memory leaks',
    link: 'https://github.com/Aspvpboss/MemTrack'
  },
  {
    title: 'SDLite library',
    language: 'C / C++',
    description: 'A lightweight SDL3 framework that removes boilerplate and provides a clean, minimal API for quick development and higher control.',
    link: 'https://github.com/Aspvpboss/SDLite'
  },
  {
    title: 'SDLite-Pong',
    language: 'C',
    description: 'Simple pong game in C using my SDLite library',
    link: 'https://github.com/Aspvpboss/Pong-SDLite'
  },
  {
    title: '3d-Voxel-Renderer',
    language: 'C++',
    description: 'A 3d renderer specialized to render cubes w/ basic lighting using OpenGL',
    link: 'https://github.com/Aspvpboss/3D-voxel-renderer'
  },

  {
    title: 'pfad-fm',
    language: 'Rust',
    description: 'A TUI & CLI cross-platform file manager written in Rust. Designed to run on minimal systems',
    link: 'https://github.com/Aspvpboss/Custom-File-Manager'
  },
  {
    title: '16-bit CPU emulator and assembler',
    language: 'C & Rust',
    description: 'A custom 16-bit CPU. The project also contains an assembler to program it',
    link: 'https://github.com/Aspvpboss/Custom-16-bit-CPU-and-Assembler'
  }
]

// Function to copy email to the clipboard
function copyEmail() {
  const email = 'b.f.vaughan2026@gmail.com'
  navigator.clipboard.writeText(email).then(() => {
    copyStatus.value = 'Copied!'
    setTimeout(() => {
      copyStatus.value = ''
    }, 2000)
  }).catch(err => {
    console.error('Failed to copy: ', err)
  })
}
</script>

<template>
  <div class="container">
    <h1>Welcome to my Portfolio!</h1>

    <!-- About Section -->
    <h2>About Me</h2>
    <p>
      A systems & graphics programming in C/C++, and Rust.
      I enjoy building tools and libraries from scratch about understanding how things work under the hood. 
    </p>

    <!-- Projects Section -->
    <h2>My GitHub Projects</h2>
    <div class="projects">
      <!-- v-for loops through our 'projects' array and renders a card for each item -->
      <div v-for="project in projects" :key="project.title" class="project">
        <h3>{{ project.title }}</h3>
        <h5>Language: {{ project.language }}</h5>
        <p>{{ project.description }}</p>
        <a :href="project.link" target="_blank">View on GitHub</a>
      </div>
    </div>

    <!-- Contact Section -->
    <h2>Contact</h2>
    <p>If you'd like to reach out, click the button to copy my email, or click the other button to go to my github:</p>
    <div class="contact">
      <!-- @click is Vue's shorthand for v-on:click -->
      <button class="copy-btn" @click="copyEmail">Copy Email</button>
      <span id="copy-status">{{ copyStatus }}</span>
      <a href="https://github.com/Aspvpboss" target="_blank">My Github</a>
    </div>

    <!-- Resume Section -->
    <h2>Resume</h2>
    <p>Get my resume here</p>
    <a href="/resume.pdf" download class="download-btn">
      Download Resume (PDF)
    </a>
  </div>
</template>
