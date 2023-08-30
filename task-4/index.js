const keyAudioMap = {
    'w': './sounds/tom-1.mp3',
    'a': './sounds/tom-2.mp3',
    's': './sounds/snare.mp3',
    'd': './sounds/tom-3.mp3',
    'j': './sounds/tom-4.mp3',
    'k': './sounds/kick-bass.mp3',
    'l': './sounds/crash.mp3'
  };
  
  function playSound(key) {
    const audio = new Audio(keyAudioMap[key]);
    audio.play();
  }
  