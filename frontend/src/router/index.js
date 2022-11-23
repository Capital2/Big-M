import { Routes, Route } from "react-router-dom";

import AppLayout from "../layout";
import Landing from "../pages/Landing";
import BigM from "../pages/BigM"

export default function RouterConfig() {
  return (
    <Routes>
      <Route path="/" element={<AppLayout />}>
        <Route index element={<Landing />} />
        <Route path="BigM" element={<BigM />} />
      </Route>
    </Routes>
  );
}
