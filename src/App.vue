<script setup>
// Array of projects — adding a new project is as simple as adding a new object here!
const projects = [
  {
    title: 'MemTrack library',
    language: 'C / C++',
    description: 'Single-header C/C++ library that tracks heap allocations and deallocations to detect and report memory leaks.',
    link: 'https://github.com/Aspvpboss/MemTrack'
  },
  {
    title: 'SDLite library',
    language: 'C / C++',
    description: 'Lightweight SDL3 framework that abstracts windowing and rendering boilerplate into a clean, minimal API for rapid development and low-level control.',
    link: 'https://github.com/Aspvpboss/SDLite'
  },
  {
    title: 'SDLite-Pong',
    language: 'C',
    description: 'Arcade Pong implementation in C demonstrating real-time game loop timing, collision detection, and rendering with SDLite.',
    link: 'https://github.com/Aspvpboss/Pong-SDLite'
  },
  {
    title: '3d-Voxel-Renderer',
    language: 'C++',
    description: 'OpenGL 3D voxel rendering engine in C++ specialized for rendering cube meshes with dynamic lighting.',
    link: 'https://github.com/Aspvpboss/3D-voxel-renderer'
  },
  {
    title: 'pfad-fm',
    language: 'Rust',
    description: 'Cross-platform TUI & CLI file manager written in Rust, engineered for speed and low resource usage on minimal systems.',
    link: 'https://github.com/Aspvpboss/Custom-File-Manager'
  },
  {
    title: '16-bit CPU emulator and assembler',
    language: 'C & Rust',
    description: 'Custom 16-bit CPU architecture emulator and accompanying assembler built from scratch to execute custom machine code.',
    link: 'https://github.com/Aspvpboss/Custom-16-bit-CPU-and-Assembler'
  }
]
</script>

<template>
  <div class="container">
    <h1>Ben Vaughan</h1>

    <!-- About Section -->
    <h2>About Me</h2>
    <p>
      Systems & graphics programmer working in C/C++ and Rust.
      I enjoy building tools, engines, and libraries from scratch to understand how things work under the hood.
    </p>

    <!-- Projects Section -->
    <h2>My GitHub Projects</h2>
    <div class="projects">
      <!-- v-for loops through our 'projects' array and renders a card for each item -->
      <div v-for="project in projects" :key="project.title" class="project">
        <h3>{{ project.title }}</h3>
        <h5>Language: {{ project.language }}</h5>
        <p>{{ project.description }}</p>
        <a :href="project.link" target="_blank" rel="noopener noreferrer">View on GitHub</a>
      </div>
    </div>

    <!-- Contact Section -->
    <h2>Contact</h2>
    <p>
      Reach out via email at
      <a href="mailto:b.f.vaughan2026@gmail.com" class="inline-link">b.f.vaughan2026@gmail.com</a>
      or check out my work on GitHub:
    </p>
    <div class="contact">
      <a href="mailto:b.f.vaughan2026@gmail.com">Email Me</a>
      <a href="https://github.com/Aspvpboss" target="_blank" rel="noopener noreferrer">My GitHub</a>
    </div>

    <!-- Resume Section -->
    <h2>Resume</h2>
    <p>Get my resume here:</p>
    <a href="/resume.pdf" target="_blank" rel="noopener noreferrer" class="download-btn">
      View Resume (PDF)
    </a>
  </div>
</template>
