<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/lux/bootstrap.min.css"
        integrity="sha384-9+PGKSqjRdkeAU7Eu4nkJU8RFaH8ace8HGXnkiKMP9I9Te0GJ4/km3L1Z8tXigpG"
        crossorigin="anonymous"
      />
      <div class="row">
        <div class="col-sm-12">
          <p class="pb-10">Library</p>
          <button type="button" class="pb-10 btn btn-success btn-sm">+</button>
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">Artist</th>
                <th scope="col">Song</th>
                <th scope="col">Played</th>
                <th scope="col">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(lib, index) in library" :key="index">
                <td class="align-middle">{{ lib.artist }}</td>
                <td class="align-middle">{{ lib.song }}</td>
                <td class="align-middle">
                  <span v-if="lib.played">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="32"
                      height="32"
                      fill="#000000"
                      viewBox="0 0 256 256"
                    >
                      <path
                        d="M229.66,77.66l-128,128a8,8,0,0,1-11.32,0l-56-56a8,8,0,0,1,11.32-11.32L96,188.69,218.34,66.34a8,8,0,0,1,11.32,11.32Z"
                      ></path>
                    </svg>
                  </span>
                  <span v-else>
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="32"
                      height="32"
                      fill="#000000"
                      viewBox="0 0 256 256"
                    >
                      <path
                        d="M205.66,194.34a8,8,0,0,1-11.32,11.32L128,139.31,61.66,205.66a8,8,0,0,1-11.32-11.32L116.69,128,50.34,61.66A8,8,0,0,1,61.66,50.34L128,116.69l66.34-66.35a8,8,0,0,1,11.32,11.32L139.31,128Z"
                      ></path>
                    </svg>
                  </span>
                </td>
                <td>
                  <div class="btn-group" role="group">
                    <button type="button" class="btn btn-info">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="25"
                        height="25"
                        fill="#000000"
                        viewBox="0 0 256 256"
                      >
                        <path
                          d="M227.31,73.37,182.63,28.68a16,16,0,0,0-22.63,0L36.69,152A15.86,15.86,0,0,0,32,163.31V208a16,16,0,0,0,16,16H92.69A15.86,15.86,0,0,0,104,219.31L227.31,96a16,16,0,0,0,0-22.63ZM92.69,208H48V163.31l88-88L180.69,120ZM192,108.68,147.31,64l24-24L216,84.68Z"
                        ></path>
                      </svg>
                    </button>
                    <button type="button" class="btn btn-danger">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="25"
                        height="25"
                        fill="#000000"
                        viewBox="0 0 256 256"
                      >
                        <path
                          d="M216,48H40a8,8,0,0,0,0,16h8V208a16,16,0,0,0,16,16H192a16,16,0,0,0,16-16V64h8a8,8,0,0,0,0-16ZM192,208H64V64H192ZM80,24a8,8,0,0,1,8-8h80a8,8,0,0,1,0,16H88A8,8,0,0,1,80,24Z"
                        ></path>
                      </svg>
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      library: [],
    };
  },

  methods: {
    getLibraries() {
      const path = "http://localhost:5000/library";
      axios
        .get(path)
        .then((res) => {
          this.library = res.data.library;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created() {
    this.getLibraries();
  },
};
</script>
