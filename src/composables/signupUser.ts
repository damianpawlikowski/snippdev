import { ref } from "vue";

import UserCredentials from "@/types/User";
import axios from "@/plugins/axios";

const useSignupUser = () => {
  const data = ref({});

  const signupUser = async (credentials: UserCredentials) => {
    const response = (await axios.post("/api/user/", credentials)).data;
    if (response) {
      data.value = response.data;
    }
  };

  return { signupUser, data };
};

export default useSignupUser;
