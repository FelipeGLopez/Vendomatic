import React from "react";

const Text = (props) => {
  const { coins, text } = props;
  return (
    <h5 style={{ margin: "2%" }}>
      Current credit: {coins} quarter coins
      <br />
      {text}
    </h5>
  );
};

export default Text;
